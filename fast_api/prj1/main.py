from fastapi import FastAPI, HTTPException
from schema import GenreURLChoice, BandBase, BandCreate, BandWithID

app = FastAPI()
    
BANDS = [
    {'id': 1, 'name': 'The Kinks', 'genre': 'Rock'},
    {'id': 2, 'name': 'Apex Twin', 'genre': 'Electronic'},
    {'id': 3, 'name': 'The Slowdive', 'genre': 'Metal', 'albums':[
        {'title': 'First Album', 'release_date': '2025-01-12'}
    ]},
    {'id': 4, 'name': 'Wu-Tang clan', 'genre': 'Hip-Hop'}
]

@app.get('/bands')
async def bands(
    genre: GenreURLChoice | None=None,
    has_album: bool = False
    ) -> list[BandWithID]:
    print(has_album)
    band_list = [BandWithID(**band) for band in BANDS]
    if genre:
        band_list = [band for band in band_list if band.genre.value.lower() == genre.value]
    if has_album:
        band_list = [band for band in band_list if len(band.albums)>0]
    return band_list

@app.get('/bands/{band_id}')
async def band(band_id: int) -> BandWithID:
    band = next((BandWithID(**band) for band in BANDS if band['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail='Band not found')
    return band

@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoice) -> list[band]:
    return [BandWithID(**band) for band in BANDS if band['genre'].lower() == genre.value]

@app.post('/bands')
async def create_band(band_data: BandCreate) -> BandWithID:
    id = BANDS[-1]['id'] + 1
    print(band_data)
    print(type(band_data))
    print(band_data.model_dump())
    band = BandWithID(id=id, **band_data.model_dump()).model_dump()
    BANDS.append(band)
    return band 
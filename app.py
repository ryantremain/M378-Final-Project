from vetiver import VetiverModel
from dotenv import load_dotenv, find_dotenv
import vetiver
import pins

load_dotenv(find_dotenv())

b = pins.board_folder('/data/model', allow_pickle_read=True)
v = VetiverModel.from_pin(b, 'penguin model', version = '20240417T070515Z-cf3d4')

vetiver_api = vetiver.VetiverAPI(v)
api = vetiver_api.app

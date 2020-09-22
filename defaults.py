# Paths
# Fill this according to own setup
BACKGROUND_DIR = 'demo_data_dir/backgrounds/'
BACKGROUND_GLOB_STRING = '*.png'
POISSON_BLENDING_DIR = '/usr1/debidatd/pb'
SELECTED_LIST_FILE = 'demo_data_dir/selected.txt'
DISTRACTOR_LIST_FILE = 'demo_data_dir/neg_list.txt' 
DISTRACTOR_DIR = 'demo_data_dir/distractor_objects_dir/'
DISTRACTOR_GLOB_STRING = '*.jpg'
INVERTED_MASK = True # Set to true if white pixels represent background

# Parameters for generator
NUMBER_OF_WORKERS = 4
BLENDING_LIST = ['none']#BLENDING_LIST = ['gaussian','poisson', 'none', 'box', 'motion']

# Parameters for images
MIN_NO_OF_OBJECTS = 1
MAX_NO_OF_OBJECTS = 8
MIN_NO_OF_DISTRACTOR_OBJECTS = 2
MAX_NO_OF_DISTRACTOR_OBJECTS = 4
WIDTH = 720
HEIGHT = 640
MAX_ATTEMPTS_TO_SYNTHESIZE = 500

# Parameters for objects in images
MIN_SCALE = 0.5 # min scale for scale augmentation
MAX_SCALE = 1.5 # max scale for scale augmentation
MAX_DEGREES = 270 # max rotation allowed during rotation augmentation
MAX_TRUNCATION_FRACTION = 0.025 # max fraction to be truncated = MAX_TRUNCACTION_FRACTION*(WIDTH/HEIGHT)
MAX_ALLOWED_IOU = 0.025 # IOU > MAX_ALLOWED_IOU is considered an occlusion
MIN_WIDTH = 6 # Minimum width of object to use for data generation
MIN_HEIGHT = 6 # Minimum height of object to use for data generation

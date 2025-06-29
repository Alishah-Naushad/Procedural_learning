"""
Default configs
"""

from yacs.config import CfgNode

# -----------------------------------------------------------------------------
# Config definition
# -----------------------------------------------------------------------------
_C = CfgNode()

# -----------------------------------------------------------------------------
# Annotation options
# -----------------------------------------------------------------------------
_C.ANNOTATION = CfgNode()

# Path to the original videos
_C.ANNOTATION.VIDEOS = ("./Datasets")

# Path to annotations
# _C.ANNOTATION.PATH = ("./Datasets/annotations/MECCANO")

# _C.ANNOTATION.PATH = ("./Datasets/annotations/PCASSEMBLY")

_C.ANNOTATION.PATH = ("./Datasets/annotations/EGTEAGAZEP/PastaSalad")


# Path to the directory containing annotations created by ELAN 6.0
_C.ANNOTATION.ELAN_DIR = ("./Datasets/annotations")

# Name of the dataset to use for generating annotation files
# Valid options are: ['CMU_Kitchens', 'EGTEA']
_C.ANNOTATION.DATASET_NAME = 'MECCANO'
# _C.ANNOTATION.DATASET_NAME = 'pc_assembly'
# _C.ANNOTATION.DATASET_NAME = 'pc_disassembly'
# _C.ANNOTATION.DATASET_NAME = 'BaconAndEggs'
# _C.ANNOTATION.DATASET_NAME = 'Pizza'
# _C.ANNOTATION.DATASET_NAME = 'Cheeseburger'
# _C.ANNOTATION.DATASET_NAME = 'ContinentalBreakfast'
# _C.ANNOTATION.DATASET_NAME = 'GreekSalad'
# _C.ANNOTATION.DATASET_NAME = 'PastaSalad'
# _C.ANNOTATION.DATASET_NAME = 'TurkeySandwich'

"""
Name of the category to use for generating annotation files
Options for CMU-MMAC: ['Eggs', 'Brownie', 'Pizza', 'Salad', 'Sandwich']
Options for EGTEAGAZEP: [
            'BaconAndEggs',
            'Cheeseburger',
            'ContinentalBreakfast',
            'GreekSalad',
            'PastaSalad',
            'Pizza',
            'TurkeySandwich',
        ]
"""
_C.ANNOTATION.CATEGORY = 'PastaSalad'  # only relevant for CMU_Kitc or EGTEA-GazeP

# -----------------------------------------------------------------------------
# Data loader options
# -----------------------------------------------------------------------------
_C.DATA_LOADER = CfgNode()

# Number of data loader workers per training process
_C.DATA_LOADER.NUM_WORKERS = 4

# Rate at which we want to sample the clips provided
_C.DATA_LOADER.SAMPLING_FPS = 2

# Size to reshape the image to before cropping
_C.DATA_LOADER.RESIZE = 256

# The spatial crop size of the input clip
_C.DATA_LOADER.CROP_SIZE = 224

# Load data to pinned host memory
# _C.DATA_LOADER.PIN_MEMORY = True
_C.DATA_LOADER.PIN_MEMORY = False

# Shuffle the data
_C.DATA_LOADER.SHUFFLE = True

# Data loader name
# Options are ['CMU_Kitchens', 'EgoProcL']
# _C.DATA_LOADER.NAME = 'MECCANO'
# _C.DATA_LOADER.NAME = 'pc_assembly'
# _C.DATA_LOADER.NAME = 'pc_disassembly'
# _C.DATA_LOADER.NAME = 'CMU_Kitchens'
# _C.DATA_LOADER.NAME = 'EPIC-Tents'
_C.DATA_LOADER.NAME = 'EGTEAGAZEP'

# -----------------------------------------------------------------------------
# Training options
# -----------------------------------------------------------------------------
_C.TRAIN = CfgNode()

# Batch size
# NOTE: Batch size greater than 1 won't work
_C.TRAIN.BATCH_SIZE = 1

# -----------------------------------------------------------------------------
# Validation options
# -----------------------------------------------------------------------------
_C.VALIDATION = CfgNode()

# Batch size
_C.VALIDATION.BATCH_SIZE = 2

# -----------------------------------------------------------------------------
# Test options
# -----------------------------------------------------------------------------
_C.TEST = CfgNode()

# Batch size
# NOTE: Batch size greater than 1 won't work
_C.TEST.BATCH_SIZE = 1

# -----------------------------------------------------------------------------
# CMU Kitchens dataset options
# -----------------------------------------------------------------------------
_C.CMU_KITCHENS = CfgNode()

_C.CMU_KITCHENS.METADATA_FILE = ("./annotations/metadata"
                                 "/CMU_Kitchens/tasks.txt")

# If the videos are in sync then we have to duplicate the egocentric annotation
# for third person videos
_C.CMU_KITCHENS.DUPLICATE_ANNOTATIONS = True

# Path to the videos
_C.CMU_KITCHENS.VIDEOS_PATH = ("./Datasets/CMU_Kitchens")

# Path to the annotations
_C.CMU_KITCHENS.ANNS_PATH = ("./annotations/"
                             "CMU_Kitchens")

# Path to save the frames
_C.CMU_KITCHENS.FRAMES_PATH = ""

# Name of the view to use for the experiment
# Options are: ['ego', 'back', 'top', 'rhs', 'lhs_top']
_C.CMU_KITCHENS.VIEW = "ego"

# -----------------------------------------------------------------------------
# EGTEA Gaze Plus dataset options
# -----------------------------------------------------------------------------
_C.EGTEA_GAZEP = CfgNode()

# Path to the videos
_C.EGTEA_GAZEP.VIDEOS_PATH = "./Datasets/EGTEAGAZEP"

# Path to the annotations
_C.EGTEA_GAZEP.ANNS_PATH = "./Datasets/annotations/EGTEAGAZEP"

# Path to save the frames
_C.EGTEA_GAZEP.FRAMES_PATH = "./Datasets/Frames/EGTEAGAZEP"



# -----------------------------------------------------------------------------
# BaconAndEggs dataset options
# -----------------------------------------------------------------------------
_C.BaconAndEggs = CfgNode()

# Path to the videos
_C.BaconAndEggs.VIDEOS_DIR = "./Datasets/EGTEAGAZEP/BaconAndEggs"

# Path to the annotations
_C.BaconAndEggs.ANNS_DIR = "./Datasets/annotations/EGTEAGAZEP/BaconAndEggs"

# Path to save the frames
_C.BaconAndEggs.FRAMES_DIR = "./Datasets/Frames/EGTEAGAZEP/BaconAndEggs"


# -----------------------------------------------------------------------------
# Pizza dataset options
# -----------------------------------------------------------------------------
_C.Pizza = CfgNode()

# Path to the videos
_C.Pizza.VIDEOS_DIR = "./Datasets/EGTEAGAZEP/Pizza"

# Path to the annotations
_C.Pizza.ANNS_DIR = "./Datasets/annotations/EGTEAGAZEP/Pizza"

# Path to save the frames
_C.Pizza.FRAMES_DIR = "./Datasets/Frames/EGTEAGAZEP/Pizza"


# -----------------------------------------------------------------------------
# Cheeseburger dataset options
# -----------------------------------------------------------------------------
_C.Cheeseburger = CfgNode()

# Path to the videos
_C.Cheeseburger.VIDEOS_DIR = "./Datasets/EGTEAGAZEP/Cheeseburger"

# Path to the annotations
_C.Cheeseburger.ANNS_DIR = "./Datasets/annotations/EGTEAGAZEP/Cheeseburger"

# Path to save the frames
_C.Cheeseburger.FRAMES_DIR = "./Datasets/Frames/EGTEAGAZEP/Cheeseburger"

# -----------------------------------------------------------------------------
# ContinentalBreakfast dataset options
# -----------------------------------------------------------------------------
_C.ContinentalBreakfast = CfgNode()

# Path to the videos
_C.ContinentalBreakfast.VIDEOS_DIR = "./Datasets/EGTEAGAZEP/ContinentalBreakfast"

# Path to the annotations
_C.ContinentalBreakfast.ANNS_DIR = "./Datasets/annotations/EGTEAGAZEP/ContinentalBreakfast"

# Path to save the frames
_C.ContinentalBreakfast.FRAMES_DIR = "./Datasets/Frames/EGTEAGAZEP/ContinentalBreakfast"


# -----------------------------------------------------------------------------
# GreekSalad dataset options
# -----------------------------------------------------------------------------
_C.GreekSalad = CfgNode()

# Path to the videos
_C.GreekSalad.VIDEOS_DIR = "./Datasets/EGTEAGAZEP/GreekSalad"

# Path to the annotations
_C.GreekSalad.ANNS_DIR = "./Datasets/annotations/EGTEAGAZEP/GreekSalad"

# Path to save the frames
_C.GreekSalad.FRAMES_DIR = "./Datasets/Frames/EGTEAGAZEP/GreekSalad"



# -----------------------------------------------------------------------------
# PastaSalad dataset options
# -----------------------------------------------------------------------------
_C.PastaSalad = CfgNode()

# Path to the videos
_C.PastaSalad.VIDEOS_DIR = "./Datasets/EGTEAGAZEP/PastaSalad"

# Path to the annotations
_C.PastaSalad.ANNS_DIR = "./Datasets/annotations/EGTEAGAZEP/PastaSalad"

# Path to save the frames
_C.PastaSalad.FRAMES_DIR = "./Datasets/Frames/EGTEAGAZEP/PastaSalad"


# -----------------------------------------------------------------------------
# TurkeySandwich dataset options
# -----------------------------------------------------------------------------
_C.TurkeySandwich = CfgNode()

# Path to the videos
_C.TurkeySandwich.VIDEOS_DIR = "./Datasets/EGTEAGAZEP/PastaSalad"

# Path to the annotations
_C.TurkeySandwich.ANNS_DIR = "./Datasets/annotations/EGTEAGAZEP/PastaSalad"

# Path to save the frames
_C.TurkeySandwich.FRAMES_DIR = "./Datasets/Frames/EGTEAGAZEP/PastaSalad"



# -----------------------------------------------------------------------------
# Brownie_ego dataset options
# -----------------------------------------------------------------------------
_C.Eggs_ego = CfgNode()

# Path to the videos
_C.Eggs_ego.VIDEOS_DIR = "./Datasets/EGTEAGAZEP/PastaSalad"

# Path to the annotations
_C.Eggs_ego.ANNS_DIR = "./Datasets/annotations/EGTEAGAZEP/PastaSalad"

# Path to save the frames
_C.Eggs_ego.FRAMES_DIR = "./Datasets/Frames/EGTEAGAZEP/PastaSalad"


# -----------------------------------------------------------------------------
# Pizza_ego dataset options
# -----------------------------------------------------------------------------
_C.Pizza_ego = CfgNode()

# Path to the videos
_C.Pizza_ego.VIDEOS_DIR = "./Datasets/EGTEAGAZEP/PastaSalad"

# Path to the annotations
_C.Pizza_ego.ANNS_DIR = "./Datasets/annotations/EGTEAGAZEP/PastaSalad"

# Path to save the frames
_C.Pizza_ego.FRAMES_DIR = "./Datasets/Frames/EGTEAGAZEP/PastaSalad"


# -----------------------------------------------------------------------------
# Sandwich_ego dataset options
# -----------------------------------------------------------------------------
_C.Sandwich_ego = CfgNode()

# Path to the videos
_C.Sandwich_ego.VIDEOS_DIR = "./Datasets/EGTEAGAZEP/PastaSalad"

# Path to the annotations
_C.Sandwich_ego.ANNS_DIR = "./Datasets/annotations/EGTEAGAZEP/PastaSalad"

# Path to save the frames
_C.Sandwich_ego.FRAMES_DIR = "./Datasets/Frames/EGTEAGAZEP/PastaSalad"


# -----------------------------------------------------------------------------
# Sandwich_ego dataset options
# -----------------------------------------------------------------------------
_C.Salad_ego = CfgNode()

# Path to the videos
_C.Salad_ego.VIDEOS_DIR = "./Datasets/EGTEAGAZEP/PastaSalad"

# Path to the annotations
_C.Salad_ego.ANNS_DIR = "./Datasets/annotations/EGTEAGAZEP/PastaSalad"

# Path to save the frames
_C.Salad_ego.FRAMES_DIR = "./Datasets/Frames/EGTEAGAZEP/PastaSalad"


# -----------------------------------------------------------------------------
# Brownie_ego dataset options
# -----------------------------------------------------------------------------
_C.Brownie_ego = CfgNode()

# Path to the videos
_C.Brownie_ego.VIDEOS_DIR = "./Datasets/EGTEAGAZEP/PastaSalad"

# Path to the annotations
_C.Brownie_ego.ANNS_DIR = "./Datasets/annotations/EGTEAGAZEP/PastaSalad"

# Path to save the frames
_C.Brownie_ego.FRAMES_DIR = "./Datasets/Frames/EGTEAGAZEP/PastaSalad"





# -----------------------------------------------------------------------------
# TCC options
# -----------------------------------------------------------------------------
_C.TCC = CfgNode()

# Path to the directory containing videos for training/testing TCC
_C.TCC.DATA_PATH = "./Datasets/MECCANO"

# Number of frames to sample from each video while training TCC
_C.TCC.NUM_FRAMES = 32

# Number of context frames to use around the main frame while training TCC
_C.TCC.NUM_CONTEXT_STEPS = 2

# Stride with which to sample the context frames
_C.TCC.CONTEXT_STRIDE = 15

# Size of the input image
_C.TCC.INPUT_SIZE = (168, 168)

# Name of the backbone model
_C.TCC.BASE_MODEL_NAME = 'resnet50'

# Use pretrained backbone while training
_C.TCC.PRETRAINED = True

# TCC Embedding size
_C.TCC.EMBEDDING_SIZE = 128

# Temperature
_C.TCC.TEMPERATURE = 0.1

# Variance lambda
_C.TCC.VARIANCE_LAMBDA = 1e-3

# Normalize video step indices for numerical stability
_C.TCC.NORMALIZE_INDICES = True

# If true, normalise the embeddings when calculating the procedure
# learning results
_C.TCC.NORMALIZE_EMBDS = True


# If true, normalise the embeddings during vava training
_C.TCC.norm_train_embeds = False

# Optimizer for TCC
_C.TCC.OPTIM_NAME = "Adam"

# Learning rate for training TCC
_C.TCC.LR = 1e-4

# Weight decay
_C.TCC.WEIGHT_DECAY = 1e-5

# Training batch size
_C.TCC.BATCH_SIZE = 2

# Training epochs
_C.TCC.TRAIN_EPOCHS = 10000

# Frequency to save checkpoint
_C.TCC.CHECKPOINT_FREQ = 1000

# Random state
_C.TCC.RANDOM_STATE = 42

# Model path for generating embeddings
_C.TCC.MODEL_PATH = ("./trained_models/TCC/")

# Path to save the embeddings
_C.TCC.EMBEDS_PATH = ("./trained_models/TCC/")

# Number of clusters to form using KMeans
_C.TCC.KMEANS_NUM_CLUSTERS = 7

# If true, perform soft KMeans
_C.TCC.GRAPH_CUT = True

# Number of frames to pass through the TCC Embedder for generating features
# _C.TCC.EMBDS_BATCH = 35
_C.TCC.EMBDS_BATCH = 20

# If true, use LSTM module with the embedder network
_C.TCC.LSTM = False

# If true, use Bi-LSTM module with the embedder network
# Note that TCC.LSTM should be True for this flag to effect
_C.TCC.BILSTM = False

# If true, use subset_selection instead of KMeans for getting the results
_C.TCC.SUBSET_SELECTION = False

# Subset size (from multitask procedure learning)
_C.TCC.SUBSET_REPNUM = 15

# If true, use LAV loss with TCC
_C.TCC.TCC_AND_LAV = False

# If true, use random predictions for results
_C.TCC.RANDOM_RESULTS = False

# coeff for push-pull loss
_C.TCC.c = 0.0001

# spread factor for laplace dist
_C.TCC.b_laplace = 2.0


# std (sqrt of var) for gauss dist
_C.TCC.gauss_dist_std = 2.0

# Directory to save the embeddings
_C.TCC.EMBDS_DIR = './embeds/'

# -----------------------------------------------------------------------------
# LAV options
# -----------------------------------------------------------------------------
_C.LAV = CfgNode()

# If true, use contrastive IDM loss for training along with TCC
_C.LAV.USE_CIDM = True

# If true do not use Soft-DTW, only use C-IDM loss
_C.LAV.ONLY_CIDM = True

# Margin
_C.LAV.LAMBDA = 2.0

# Window size
# Default to 10 seconds (30 fps) for CMU Kitchens
_C.LAV.SIGMA = 300.0

# Contribution weight of temporal regularisation when using with SoftDTW
_C.LAV.ALPHA = 1.0

# Contribution percent of temporal regularisation when adding with TCC
_C.LAV.CONTRIB_PERCENT = 1.0

# Random state
_C.LAV.RANDOM_STATE = 42

# Path to the directory containing videos for training/testing LAV
_C.LAV.DATA_PATH = "./Datasets/MECCANO"

# Size of the input image
_C.LAV.INPUT_SIZE = (168, 168)

# Training batch size
_C.LAV.BATCH_SIZE = 5

# Number of frames to sample from each video while training using LAV
_C.LAV.NUM_FRAMES = 32

# Number of context frames to use around the main frame while training LAV
_C.LAV.NUM_CONTEXT_STEPS = 2

# Stride with which to sample the context frames
_C.LAV.CONTEXT_STRIDE = 15

# Training epochs
_C.LAV.TRAIN_EPOCHS = 10000

# Frequency to save checkpoint
_C.LAV.CHECKPOINT_FREQ = 500

# -----------------------------------------------------------------------------
# Miscellaneous definition
# -----------------------------------------------------------------------------
_C.MISC = CfgNode()

# Print detailed output of steps taking place
_C.MISC.VERBOSE = False

# Visualise the frames obtained for debugging the data loader
_C.MISC.DEBUG_VIZ = False

# Path to the folder where frames for debugging the data loader are to be
# saved
_C.MISC.DEBUG_VIZ_PATH = "./XYZ/Desktop"

# GPU ID. Required at some places
_C.MISC.GPU_ID = 0

# If true, stop the code at various breakpoints. To be used for debugging.
_C.MISC.DEBUG = False

# If true, do not visualise the procedure learning results
_C.MISC.SAVE_TIME = False

# IF true, evaluate per-keystep else overall
_C.MISC.EVAL_PER_KEYSTEP = True

# -----------------------------------------------------------------------------
# Options for representation learning
# -----------------------------------------------------------------------------
_C.REP_LEARN = CfgNode()

# Alpha for graph cut
# Determines the cost of assigning different labels to neighbors
_C.REP_LEARN.GRAPH_CUT_ALPHA = 5

# Beta for graph cut
# Scales the cost of assigning labels to frames
_C.REP_LEARN.GRAPH_CUT_BETA = 0.2

# -----------------------------------------------------------------------------
# Logging options
# -----------------------------------------------------------------------------
_C.LOG = CfgNode()

# Path to the directory to save all the outputs from an experiment (including
# visualisations, logs, results, etc.)
_C.LOG.DIR = None

# Level of logging to use
# Options are: ['debug', 'info', 'warning', 'error', 'critical', None]
_C.LOG.LEVEL = "debug"

# If path to a csv is provided, save individual procedure learning experiment's
# results in a CSV file
_C.LOG.SAVE_CUMULATIVE_RESULTS = ''

# If true, bypass the log directory presence check. Useful when debugging
_C.LOG.BYPASS = False

# If true, save the results to the CSV using the original metric
_C.LOG.USE_ORIGINAL_METRICS = False

# -----------------------------------------------------------------------------
# ProceL dataset options
# -----------------------------------------------------------------------------
_C.PROCEL = CfgNode()

# Path to the directory containing the videos
_C.PROCEL.VIDEOS_DIR = './Datasets/ProceL/videos'

# Name of the category for which we want to do the experiments
_C.PROCEL.CATEGORY = 'make_smoke_salmon_sandwich'

# Path to the directory for saving the frames
_C.PROCEL.FRAMES_DIR = './Datasets/ProceL/frames'

# Path to the directory containing the annotations
_C.PROCEL.ANNS_DIR = './Datasets/ProceL/annotations'

# -----------------------------------------------------------------------------
# MECCANO dataset options
# -----------------------------------------------------------------------------
_C.MECCANO = CfgNode()

# Path to the directory containing the videos
_C.MECCANO.VIDEOS_DIR = './Datasets/MECCANO'

# Path to the directory for saving the frames
_C.MECCANO.FRAMES_DIR = './Datasets/Frames/MECCANO'

# Path to the directory contatining the annotations
_C.MECCANO.ANNS_DIR = './Datasets/annotations/MECCANO'

# -----------------------------------------------------------------------------
# EPIC-Tents dataset options
# -----------------------------------------------------------------------------
_C.TENTS = CfgNode()

# Path to the directory containing the videos
_C.TENTS.VIDEOS_DIR = './Datasets/EPIC-Tents/videos'

# Path to the directory for saving the frames
_C.TENTS.FRAMES_DIR = './Datasets/EPIC-Tents/frames'

# Path to the directory contatining the annotations
_C.TENTS.ANNS_DIR = './Datasets/annotations/EPIC-Tents'


# -----------------------------------------------------------------------------
# CrossTask dataset options
# -----------------------------------------------------------------------------
_C.CROSSTASK = CfgNode()

# Path to the directory containing the videos
_C.CROSSTASK.VIDEOS_DIR = './Datasets/CrossTask/videos'

# Name of the category for which we want to do the experiments
_C.CROSSTASK.CATEGORY = 105253

# Path to the directory for saving the frames
_C.CROSSTASK.FRAMES_DIR = './Datasets/CrossTask/frames'

# Path to the directory containing the annotations
_C.CROSSTASK.ANNS_DIR = './Datasets/CrossTask/annotations'


# -----------------------------------------------------------------------------
# PC Assembly dataset options
# -----------------------------------------------------------------------------
_C.PCASSEMBLY = CfgNode()

# Path to the directory containing the videos
_C.PCASSEMBLY.VIDEOS_DIR = './Datasets/pc_assembly/videos'

# Path to the directory for saving the frames
_C.PCASSEMBLY.FRAMES_DIR = './Datasets/pc_assembly/frames'

# Path to the directory contatining the annotations
_C.PCASSEMBLY.ANNS_DIR = './Datasets/pc_assembly/annotations'


# -----------------------------------------------------------------------------
# PC Disassembly dataset options
# -----------------------------------------------------------------------------
_C.PCDISASSEMBLY = CfgNode()

# Path to the directory containing the videos
_C.PCDISASSEMBLY.VIDEOS_DIR = './Datasets/pc_disassembly/videos'

# Path to the directory for saving the frames
_C.PCDISASSEMBLY.FRAMES_DIR = './Datasets/pc_disassembly/frames'

# Path to the directory contatining the annotations
_C.PCDISASSEMBLY.ANNS_DIR = './Datasets/pc_disassembly/annotations'


def get_cfg_defaults():
    """
    Get a yacs CfgNode object with default values
    """
    return _C.clone()

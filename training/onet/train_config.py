import config

class TrainConfig(object):
    def __init__(self):
        super(TrainConfig, self).__init__()
        #  ------------ General options ----------------------------------------
        self.save_path = "./results/onet/"
        self.dataPath = "/home/ubuntu/dataset/WIDER/WIDER_train/images"  # path for loading data set
        self.annoPath = "./annotations/{0}_landmarks_imglist_anno_48.txt".format(config.NUM_LANDMARKS)
        self.manualSeed = 1  # manually set RNG seed
        self.use_cuda = True
        self.GPU = "0"  # default gpu to use

        # ------------- Data options -------------------------------------------
        self.nThreads = 8  # number of data loader threads

        # ---------- Optimization options --------------------------------------
        self.nEpochs = 50  # number of total epochs to train 400
        self.batchSize = 2048  # mini-batch size 128

        # lr master for optimizer 1 (mask vector d)
        self.lr = 0.001  # initial learning rate
        self.step = [10, 25, 40]  # step for linear or exp learning rate policy
        self.decayRate = 0.1  # lr decay rate
        self.endlr = -1

        # ---------- Model options ---------------------------------------------
        self.experimentID = "072602"

        # ---------- Resume or Retrain options ---------------------------------------------
        self.resume = None  # "./checkpoint_064.pth"
        self.retrain = None

        # self.save_path = self.save_path + "log_bs{:d}_lr{:.3f}_{}/".format(self.batchSize, self.lr, self.experimentID)
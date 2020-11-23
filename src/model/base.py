from torch import nn
import logging

from utils import helper

def makeFromTemplate(inChan, outChan, hiddenDim, growList,
                    *args, **kwargs):
    layers = []
    tmpIn = inChan
    for i, g in enumerate(growList):
        tmpOut = tmpIn*growList[i]
        layers.append(makeBlock(inChan=tmpIn,
                                outChan=tmpOut,
                                isFinalLayer=False,
                                *args, **kwargs))
        tmpIn = tmpOut
    layers.append(makeBlock(inChan=tmpIn,
                            outChan=outChan,
                            isFinalLayer=True,
                            *args, **kwargs))
    seq = nn.Sequential(*layers)
    logging.debug('inChan: {}\n\
                  outChan: {}\n\
                  hiddenDim: {}\n\
                  growList: {}\n\
                  args: {}\n\
                  kwargs: {}\n\
                  Seq:\n{}'.format(inChan, outChan, hiddenDim,\
                                   helper.listToStr(growList),\
                                   helper.listToStr(args),\
                                   helper.dictToStr(kwargs),\
                                   helper.listToStr(seq)))
    return seq

def makeBlock(inChan, outChan, isFinalLayer,
                 *args, **kwargs):
    ksize  = kwargs.get('ksize', 4)
    stride = kwargs.get('stride', 1)

    layers = [
        nn.ConvTranspose2d(inChan, outChan, ksize, stride)
    ]
    if not isFinalLayer:
        layers.append(nn.BatchNorm2d(outChan))
        layers.append(nn.ReLU(inplace=True))
    else:
        layers.append(nn.Tanh())
    seq = nn.Sequential(*layers)

    logging.debug('inChan: {}\n\
                  outChan: {}\n\
                  args: {}\n\
                  kwargs: {}\n\
                  Seq:\n{}'.format(inChan, outChan,\
                                   helper.listToStr(args),\
                                   helper.dictToStr(kwargs),\
                                   helper.listToStr(seq)))
    return seq

class Generator(nn.Module):
    '''
    Generator class
    '''

    def __init__(self, zDim=10, imChan=1, hiddenDim=64, growList=[4, 4, 2]):
        super(Generator, self).__init__()
        self.zDim = zDim
        self.gen = makeFromTemplate(inChan=zDim,
                                    growList=growList,
                                    hiddenDim=hiddenDim,
                                    outChan=imChan)
        logging.info('generator: {}'.format(self.gen))


if __name__ == '__main__':
    helper.setup_logging()
    logging.info('started logger')

    Generator()

from scriptGen.entity import entity_gen
from scriptGen.imapper import imapper_gen

if __name__ == '__main__':
    entity_gen('authorize', 'preloan_validation_rist_iterms')
    imapper_gen('authorize', 'preloan_validation_rist_iterms')

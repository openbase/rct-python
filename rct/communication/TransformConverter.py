'''
Created on Apr 13, 2015

@author: nkoester
'''
import time

from rsb.converter import Converter, ProtocolBufferConverter

from rct.core.Affine3d import Affine3d
from rct.core.Transform import Transform
from openbase.type.geometry.FrameTransform_pb2 import FrameTransform
from pyrr import Quaternion, Vector4


class TransformConverter(Converter):

    '''
    classdocs
    '''

    __internal_converter = None

    def __init__(self):
        '''
        Constructor
        '''
        self.__internal_converter = ProtocolBufferConverter(FrameTransform)
        super(TransformConverter, self).__init__(bytearray, Transform, self.__internal_converter.getWireSchema())

    def serialize(self, data):
        frame_transform = self.domain_to_RST(data)
        serialized = self.__internal_converter.serialize(frame_transform)
        return serialized

    def deserialize(self, data, wireSchema):
        frame_transform = self.__internal_converter.deserialize(data, wireSchema)
        transform = self.rst_to_domain(frame_transform)
        return transform

    def domain_to_RST(self, transform):
        frame_transform = FrameTransform()
        frame_transform.frame_parent = transform.frame_parent
        frame_transform.frame_child = transform.frame_child
        frame_transform.time.time = int(time.time() * 1000000)
        frame_transform.transform.translation.x = transform.transformation.translation.x
        frame_transform.transform.translation.y = transform.transformation.translation.y
        frame_transform.transform.translation.z = transform.transformation.translation.z
        frame_transform.transform.rotation.qw = transform.transformation.rotation_quaternion.w
        frame_transform.transform.rotation.qx = transform.transformation.rotation_quaternion.x
        frame_transform.transform.rotation.qy = transform.transformation.rotation_quaternion.y
        frame_transform.transform.rotation.qz = transform.transformation.rotation_quaternion.z
        return frame_transform

    def rst_to_domain(self, frame_transform):
        position_vector = Vector4()
        position_vector.x = frame_transform.transform.translation.x
        position_vector.y = frame_transform.transform.translation.y
        position_vector.z = frame_transform.transform.translation.z
        # because it's a vector
        position_vector.w = 0.

        rotation_quaterniond = Quaternion()
        rotation_quaterniond.w = frame_transform.transform.rotation.qw
        rotation_quaterniond.x = frame_transform.transform.rotation.qx
        rotation_quaterniond.y = frame_transform.transform.rotation.qy
        rotation_quaterniond.z = frame_transform.transform.rotation.qz

        scale = Vector4([1., 1., 1., 1.])

        new_transformation = Affine3d(position_vector, rotation_quaterniond, scale)

        transform = Transform(new_transformation,
                              frame_transform.frame_parent,
                              frame_transform.frame_child,
                              time.time())
        return transform

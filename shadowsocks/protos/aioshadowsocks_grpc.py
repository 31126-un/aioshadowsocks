# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: shadowsocks/protos/aioshadowsocks.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.client
import grpclib.const

if typing.TYPE_CHECKING:
    import grpclib.server

import shadowsocks.protos.aioshadowsocks_pb2


class ssBase(abc.ABC):
    @abc.abstractmethod
    async def CreateUser(
        self,
        stream: "grpclib.server.Stream[shadowsocks.protos.aioshadowsocks_pb2.UserReq, shadowsocks.protos.aioshadowsocks_pb2.User]",
    ) -> None:
        pass

    @abc.abstractmethod
    async def UpdateUser(
        self,
        stream: "grpclib.server.Stream[shadowsocks.protos.aioshadowsocks_pb2.UserReq, shadowsocks.protos.aioshadowsocks_pb2.User]",
    ) -> None:
        pass

    @abc.abstractmethod
    async def GetUser(
        self,
        stream: "grpclib.server.Stream[shadowsocks.protos.aioshadowsocks_pb2.UserIdReq, shadowsocks.protos.aioshadowsocks_pb2.User]",
    ) -> None:
        pass

    @abc.abstractmethod
    async def DeleteUser(
        self,
        stream: "grpclib.server.Stream[shadowsocks.protos.aioshadowsocks_pb2.UserIdReq, shadowsocks.protos.aioshadowsocks_pb2.Empty]",
    ) -> None:
        pass

    @abc.abstractmethod
    async def ListUser(
        self,
        stream: "grpclib.server.Stream[shadowsocks.protos.aioshadowsocks_pb2.UserReq, shadowsocks.protos.aioshadowsocks_pb2.UserList]",
    ) -> None:
        pass

    @abc.abstractmethod
    async def HealthCheck(
        self,
        stream: "grpclib.server.Stream[shadowsocks.protos.aioshadowsocks_pb2.HealthCheckReq, shadowsocks.protos.aioshadowsocks_pb2.HealthCheckRes]",
    ) -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            "/aioshadowsocks.ss/CreateUser": grpclib.const.Handler(
                self.CreateUser,
                grpclib.const.Cardinality.UNARY_UNARY,
                shadowsocks.protos.aioshadowsocks_pb2.UserReq,
                shadowsocks.protos.aioshadowsocks_pb2.User,
            ),
            "/aioshadowsocks.ss/UpdateUser": grpclib.const.Handler(
                self.UpdateUser,
                grpclib.const.Cardinality.UNARY_UNARY,
                shadowsocks.protos.aioshadowsocks_pb2.UserReq,
                shadowsocks.protos.aioshadowsocks_pb2.User,
            ),
            "/aioshadowsocks.ss/GetUser": grpclib.const.Handler(
                self.GetUser,
                grpclib.const.Cardinality.UNARY_UNARY,
                shadowsocks.protos.aioshadowsocks_pb2.UserIdReq,
                shadowsocks.protos.aioshadowsocks_pb2.User,
            ),
            "/aioshadowsocks.ss/DeleteUser": grpclib.const.Handler(
                self.DeleteUser,
                grpclib.const.Cardinality.UNARY_UNARY,
                shadowsocks.protos.aioshadowsocks_pb2.UserIdReq,
                shadowsocks.protos.aioshadowsocks_pb2.Empty,
            ),
            "/aioshadowsocks.ss/ListUser": grpclib.const.Handler(
                self.ListUser,
                grpclib.const.Cardinality.UNARY_UNARY,
                shadowsocks.protos.aioshadowsocks_pb2.UserReq,
                shadowsocks.protos.aioshadowsocks_pb2.UserList,
            ),
            "/aioshadowsocks.ss/HealthCheck": grpclib.const.Handler(
                self.HealthCheck,
                grpclib.const.Cardinality.UNARY_UNARY,
                shadowsocks.protos.aioshadowsocks_pb2.HealthCheckReq,
                shadowsocks.protos.aioshadowsocks_pb2.HealthCheckRes,
            ),
        }


class ssStub:
    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateUser = grpclib.client.UnaryUnaryMethod(
            channel,
            "/aioshadowsocks.ss/CreateUser",
            shadowsocks.protos.aioshadowsocks_pb2.UserReq,
            shadowsocks.protos.aioshadowsocks_pb2.User,
        )
        self.UpdateUser = grpclib.client.UnaryUnaryMethod(
            channel,
            "/aioshadowsocks.ss/UpdateUser",
            shadowsocks.protos.aioshadowsocks_pb2.UserReq,
            shadowsocks.protos.aioshadowsocks_pb2.User,
        )
        self.GetUser = grpclib.client.UnaryUnaryMethod(
            channel,
            "/aioshadowsocks.ss/GetUser",
            shadowsocks.protos.aioshadowsocks_pb2.UserIdReq,
            shadowsocks.protos.aioshadowsocks_pb2.User,
        )
        self.DeleteUser = grpclib.client.UnaryUnaryMethod(
            channel,
            "/aioshadowsocks.ss/DeleteUser",
            shadowsocks.protos.aioshadowsocks_pb2.UserIdReq,
            shadowsocks.protos.aioshadowsocks_pb2.Empty,
        )
        self.ListUser = grpclib.client.UnaryUnaryMethod(
            channel,
            "/aioshadowsocks.ss/ListUser",
            shadowsocks.protos.aioshadowsocks_pb2.UserReq,
            shadowsocks.protos.aioshadowsocks_pb2.UserList,
        )
        self.HealthCheck = grpclib.client.UnaryUnaryMethod(
            channel,
            "/aioshadowsocks.ss/HealthCheck",
            shadowsocks.protos.aioshadowsocks_pb2.HealthCheckReq,
            shadowsocks.protos.aioshadowsocks_pb2.HealthCheckRes,
        )

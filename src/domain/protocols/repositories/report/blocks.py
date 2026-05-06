from typing import Protocol

from src.domain.protocols.methods import BulkAddMixinProtocol


class BlockRepositoryProtocol(BulkAddMixinProtocol, Protocol): ...


class ReportSingleRepositoryProtocol(BlockRepositoryProtocol, Protocol): ...


class ReportTableRepositoryProtocol(BlockRepositoryProtocol, Protocol): ...

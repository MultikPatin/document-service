from typing import Protocol

from src.core.protocols.repository_methods import BulkAddMixinProtocol


class BlockRepositoryProtocol(BulkAddMixinProtocol, Protocol): ...


class ReportSingleRepositoryProtocol(BlockRepositoryProtocol, Protocol): ...


class ReportTableRepositoryProtocol(BlockRepositoryProtocol, Protocol): ...

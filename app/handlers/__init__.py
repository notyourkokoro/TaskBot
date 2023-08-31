from .start_command import start_router
from .help_command import help_router
from .task_command import task_router
from .tasks_command import tasks_router
from .pass_handler import pass_router
from .not_completed_handler import not_completed_router

routers_list = [
    pass_router,
    not_completed_router,
    task_router,
    tasks_router,
    start_router,
    help_router
]

__all__ = ['routers_list']
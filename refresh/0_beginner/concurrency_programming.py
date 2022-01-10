"""
concurrency in python (1.*, 2.*, 3.* )

3.2+ concurrent.futures
    1.5+ threading
    2.6+ multiprocessing

3.4+ asyncio
"""

"""
Moore's law -> end of moore's law?
from single to -> multitask -> multicore
1. monolith
2. one guy doing everything
3. teamwork
"""

"""
Concepts:
    - order of execution does not affect the eventual outcome
    - shared resources, as much as possible require coordination (keep a threshold) 
    - design patterns: 
        parallel / (same time same task) 
        async program / (same time, chunk of task, subtask)
        map - reduce
"""


def monolith():
    """
    code is single threaded

    run
    ```pytest```
    """
    # import pytest
    # pytest.main(['-s', './lib/thumbnail.test.py'])
    from lib.thumbnail import ThumbnailMakerService, IMG_URLS
    tn_maker = ThumbnailMakerService()
    tn_maker.make_thumbnails(IMG_URLS)
    pass


def download():
    pass


def rescale():
    pass


if __name__ == "__main__":
    monolith()

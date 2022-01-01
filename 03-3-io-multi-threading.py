# https://docs.python.org/3.7/library/concurrent.futures.html#concurrent.futures.ThreadExecutor
import 


def fetcher(params):
    session = params[0]
    url = params[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url)
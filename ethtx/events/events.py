#  Copyright 2021 DAI Foundation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at: http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import logging
import time

log = logging.getLogger(__name__)


class EthTxEvents:
    def __init__(self):
        pass

    def record(self, f):
        def decorator(*args, **kwargs):
            time_start = time.time()
            func_o = f(*args, **kwargs)

            return func_o

        return decorator

    def push(self, metric_name: str):
        def decorator(f):
            def wrapper(*args, **kwargs):
                func_o = f(*args, **kwargs)
                data = {metric_name: func_o}

                return func_o

            return wrapper

        return decorator

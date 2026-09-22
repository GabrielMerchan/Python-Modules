#!/usr/bin/env python3

from typing import Any
import abc


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._counter: int = 0
 
    @abc.abstractmethod
    def validate(self, data: Any) -> bool:
        pass
 
    @abc.abstractmethod
    def ingest(self, data: Any) -> None:
        pass
 
    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data left on processor")
        return self._data.pop(0)
 
    def _store(self, value: str) -> None:
        self._data.append((self._counter, value))
        self._counter += 1
 
 
class NumericProcessor(DataProcessor):
    def _is_number(self, x: Any) -> bool:
        return isinstance(x, (int, float)) and not isinstance(x, bool)
 
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(self._is_number(x) for x in data)
        return self._is_number(data)
 
    def ingest(self, data: int | float | list[int] |
               list[float] | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for x in items:
            self._store(str(x))
 
 
class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return isinstance(data, str)
 
    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items = data if isinstance(data, list) else [data]
        for x in items:
            self._store(x)
 
 
class LogProcessor(DataProcessor):
    def _is_log(self, x: Any) -> bool:
        return (isinstance(x, dict)
                and "log_level" in x
                and "log_message" in x
                and all(isinstance(k, str) and isinstance(v, str)
                        for k, v in x.items()))
 
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(self._is_log(x) for x in data)
        return self._is_log(data)
 
    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for x in items:
            self._store(f"{x['log_level']}: {x['log_message']}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
 
    print("\nTesting Numeric Processor...")
    numeric = NumericProcessor()
    print(f" Trying to validate input '42': {numeric.validate(42)}")
    print(f" Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except ValueError as e:
        print(f" Got exception: {e}")
    numeric_data = [1, 2, 3, 4, 5]
    print(f" Processing data: {numeric_data}")
    numeric.ingest(numeric_data)
    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric.output()
        print(f" Numeric value {rank}: {value}")
 
    print("\nTesting Text Processor...")
    text = TextProcessor()
    print(f" Trying to validate input 'Hello': {text.validate('Hello')}")
    print(f" Trying to validate input '42': {text.validate(42)}")
    text_data = ["Hello", "Nexus", "World"]
    print(f" Processing data: {text_data}")
    text.ingest(text_data)
    print(" Extracting 1 value...")
    rank, value = text.output()
    print(f" Text value {rank}: {value}")
 
    print("\nTesting Log Processor...")
    log = LogProcessor()
    valid_log = {"log_level": "INFO", "log_message": "System ready"}
    print(f" Trying to validate input '{valid_log}': "
          f"{log.validate(valid_log)}")
    print(f" Trying to validate input 'Hello': {log.validate('Hello')}")
    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f" Processing data: {log_data}")
    log.ingest(log_data)
    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f" Log entry {rank}: {value}")

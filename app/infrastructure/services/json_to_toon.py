from typing import Union, Dict, List, Any

class JSONtoTOON:
    def __init__(self, indent_size: int = 2) -> None:
        self.indent_size = indent_size
    
    def convert(self, json_data: Union[Dict[str, Any], List[str], Any], indent_level: int = 0) -> str: # type: ignore
        if isinstance(json_data, dict):
            return self._convert_dict(json_data, indent_level) # type: ignore
        elif isinstance(json_data, list):
            return self._convert_list(json_data, indent_level) # type: ignore
        else:
            return self._convert_primitive(json_data)
    
    def _convert_dict(self, data: Dict[str, Any], indent_level: int) -> str:
        if not data:
            return "{}"
        
        next_indent: str = " " * ((indent_level + 1) * self.indent_size)
        result: List[str] = []
        
        for key, value in data.items():
            if isinstance(value, dict):
                result.append(f"{next_indent}{key}:")
                result.append(self._convert_dict(value, indent_level + 1)) # type: ignore
            elif isinstance(value, list):
                result.append(f"{next_indent}{key}:")
                result.append(self._convert_list(value, indent_level + 1)) # type: ignore
            else:
                result.append(f"{next_indent}{key}: {self._convert_primitive(value)}")
        
        return "\n".join(result)
    
    def _convert_list(self, data: List[Any], indent_level: int) -> str:
        if not data:
            return "[]"
        
        next_indent: str = " " * ((indent_level + 1) * self.indent_size)
        result: List[str] = []
        
        for item in data:
            if isinstance(item, dict):
                dict_lines: List[str] = []
                for i, (key, value) in enumerate(item.items()): # type: ignore
                    prefix: str = "- " if i == 0 else "  "
                    if isinstance(value, dict):
                        dict_lines.append(f"{next_indent}{prefix}{key}:")
                        dict_lines.append(self._convert_dict(value, indent_level + 1)) # type: ignore
                    elif isinstance(value, list):
                        dict_lines.append(f"{next_indent}{prefix}{key}:")
                        dict_lines.append(self._convert_list(value, indent_level + 1)) # type: ignore
                    else:
                        dict_lines.append(f"{next_indent}{prefix}{key}: {self._convert_primitive(value)}")
                result.extend(dict_lines)
            elif isinstance(item, list):
                result.append(f"{next_indent}-")
                result.append(self._convert_list(item, indent_level + 1)) # type: ignore
            else:
                result.append(f"{next_indent}- {self._convert_primitive(item)}")
        
        return "\n".join(result)
    
    def _convert_primitive(self, value: Any) -> str:
        if value is None:
            return "null"
        elif isinstance(value, bool):
            return "true" if value else "false"
        elif isinstance(value, str):
            if '"' in value or '\n' in value:
                return f'"{value}"'
            return value
        else:
            return str(value)
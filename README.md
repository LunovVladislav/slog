# slog
Simple logging python library

"-" symbol is functional and therefore can not be used in tags or messages

```python
from log import Log

#set file name
log = Log("app") # the name is set to be app.log

log.info("info message")
log.warning("warning message")
log.debug("debug message")
log.error("error message")
log.log("custom tag", "message with custom tag")

"""
error-wow-04/06/2021 14:15:17
info-info message-04/06/2021 14:26:25
warning-warning message-04/06/2021 14:26:25
debug-debug message-04/06/2021 14:26:25
error-error message-04/06/2021 14:26:25
custom tag-message with custom tag-04/06/2021 14:26:25
"""
```

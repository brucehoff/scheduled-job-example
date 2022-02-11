FROM sagebionetworks/synapsepythonclient

COPY list_files.py list_files.py
CMD python3 list_files.py

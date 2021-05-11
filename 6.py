# never port a python project from pc to mac every again
# ModuleNotFoundError: No module named '_cffi_backend'
# webdevjs-MacBook-Pro:snack webdevj$ env/bin/pip install -U cffi
# Requirement already satisfied: cffi in ./env/lib/python3.7/site-packages (1.14.0)
# Collecting cffi
#   Downloading cffi-1.14.5-cp37-cp37m-macosx_10_9_x86_64.whl (176 kB)
#      |████████████████████████████████| 176 kB 172 kB/s 
# Requirement already satisfied: pycparser in ./env/lib/python3.7/site-packages (from cffi) (2.19)
# Installing collected packages: cffi
#   Attempting uninstall: cffi
#     Found existing installation: cffi 1.14.0
#     Uninstalling cffi-1.14.0:
#       Successfully uninstalled cffi-1.14.0
# Successfully installed cffi-1.14.5
# webdevjs-MacBook-Pro:snack webdevj$ env/bin/python -m snack.main
# 2021-05-11 02:39:44,183 [INFO    ] main.main: Starting Snack v3.0.4.
# 2021-05-11 02:39:44,189 [INFO    ] effects.get_pdf_paths: DRY RUN: get_pdf_paths(), inbox is inbox
# 2021-05-11 02:39:44,191 [INFO    ]  extract.scan_from_pdf: Extracting scan from inbox/JamesTEST_44.pdf.
# 2021-05-11 02:39:44,193 [INFO    ]  extract.scan_from_pdf: Extracting xml with tika...
# 2021-05-11 02:39:44,202 [INFO    ]       tika.getRemoteJar: Retrieving http://search.maven.org/remotecontent?filepath=org/apache/tika/tika-server/1.23/tika-server-1.23.jar to /var/folders/60/45h_vjpx29z59733dgmd_p440000gn/T/tika-server.jar.




# 2021-05-11 02:46:03,186 [INFO    ]        tika.getRemoteJar: Retrieving http://search.maven.org/remotecontent?filepath=org/apache/tika/tika-server/1.23/tika-server-1.23.jar.md5 to /var/folders/60/45h_vjpx29z59733dgmd_p440000gn/T/tika-server.jar.md5.
# 2021-05-11 02:46:04,632 [WARNING ]       tika.startServer: Failed to see startup log message; retrying...
# 2021-05-11 02:46:09,639 [WARNING ]       tika.startServer: Failed to see startup log message; retrying...
# 2021-05-11 02:46:14,656 [WARNING ]       tika.startServer: Failed to see startup log message; retrying...
# 2021-05-11 02:46:19,663 [ERROR   ]       tika.startServer: Tika startup log message not received after 3 tries.
# 2021-05-11 02:46:19,666 [ERROR   ]      tika.checkTikaServer: Failed to receive startup confirmation from startServer.
# 2021-05-11 02:46:19,669 [ERROR   ]  main.process_pdf: Failed extracting text/barcodes from inbox/JamesTEST_44.pdf.
# Traceback (most recent call last):
#   File "/Users/webdevj/webdevj/snack/snack/main.py", line 80, in process_pdf
#     scan = extract.scan_from_pdf(pdf_path)
#   File "/Users/webdevj/webdevj/snack/snack/extract.py", line 32, in scan_from_pdf
#     pdf_data = tika.parser.from_file(pdf_path, xmlContent=True)
#   File "/Users/webdevj/webdevj/snack/env/lib/python3.7/site-packages/tika/parser.py", line 39, in from_file
#     headers=headers, config_path=config_path, requestOptions=requestOptions)
#   File "/Users/webdevj/webdevj/snack/env/lib/python3.7/site-packages/tika/tika.py", line 331, in parse1
#     rawResponse=rawResponse, requestOptions=requestOptions)
#   File "/Users/webdevj/webdevj/snack/env/lib/python3.7/site-packages/tika/tika.py", line 524, in callServer
#     serverEndpoint = checkTikaServer(scheme, serverHost, port, tikaServerJar, classpath, config_path)
#   File "/Users/webdevj/webdevj/snack/env/lib/python3.7/site-packages/tika/tika.py", line 594, in checkTikaServer
#     raise RuntimeError("Unable to start Tika server.")
# RuntimeError: Unable to start Tika server.
# 2021-05-11 02:46:19,671 [INFO    ] effects.archive_scan: DRY RUN: archive_scan(inbox/

# need Java 8 for tiki server
# 1st version
# def log_request(req: 'flask_request', res: str) -> None:
#     with open('vsearch.log','a') as log:
#         print(req, res, file=log)
#
# 2nd version with end parameter
# def log_request(req: 'flask_request', res: str) -> None:
#     with open('vsearch.log', 'a') as log:
#         print(req.form, file= log, end= '|') # the optional end argument allows to specify '|' instead of a default new linw
#         print(req.remote_addr, file = log, end= '|')
#         print(req.user_agent, file = log, end= '|')
#         print( res, file=log)

# 3rd version with seq parameter
def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        # seq parameter - specify a separation value to be used when printing multiple values in a single call to print.
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

import asyncio

from task2.storage import check_if_in_storage, insert_in_storage, get_one_from_storage, get_from_storage
from task2.storage import create_short_link

user_list = []



async def app(scope, receive, send):

    if scope['client'][0] in user_list:
        await asyncio.sleep(3)
    else:
        user_list.append(scope['client'][0])

    if scope['type'] == 'http':

        if scope['method'] == 'GET':

            scope_path = scope['path'][1:]
            url_storage_list = list((await get_from_storage()).values())

            if scope_path in url_storage_list:

                url = await get_one_from_storage(scope_path)
                response_header = [(b'Location', url[0].encode())]

                await send({
                    'type': 'http.response.start',
                    'status': 301,
                    'headers': response_header
                })

                return

            else:

                await send({
                    'type': 'http.response.start',
                    'status': 200
                })

                return

    if scope['method'] == 'POST':

        post_request = await receive()

        if post_request["body"]:
            body = str(post_request["body"]).replace("b","",1)[1:-1]

            if await check_if_in_storage(body):

                await send({
                    'type': 'http.response.start',
                    'status': 400
                })

                await send({
                    'type': 'http.response.body',
                    'body': b'Already exist',
                    'status': 400
                })

                return

            else:

                server_info = str(scope['server'][0]) + ':' + str(scope['server'][1])
                insert = await insert_in_storage(body, server_info)

                await send({
                    'type': 'http.response.start',
                    'status': 201
                })

                await send({
                    'type': 'http.response.body',
                    'status': 201,
                    'body': b'Your link - ' + insert.encode()
                })

                return

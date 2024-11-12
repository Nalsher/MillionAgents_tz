from task2.shortlink import create_short_link

async def insert_in_storage(link:str, server_info: str) -> str:

    with open("storage.txt", "a+") as file:

        shortlink = await create_short_link(link)
        file.write(link + " " + shortlink + "\n")

    return server_info + '/' + shortlink

async def get_from_storage() -> dict:

    dict_with_links = {}

    with open("storage.txt", "r+") as file:

        file_content = file.readlines()

        for i in file_content:

            i = i.replace("\n","")
            i = i.split(" ")

            dict_with_links[i[0]] = i[1]

    return dict_with_links

async def check_if_in_storage(link:str) -> bool:

    all_links = await get_from_storage()

    if all_links.get(link):
        return True

    return False

async def get_one_from_storage(shortlink: str) -> dict:

    all_links = await get_from_storage()

    for i in all_links.keys():
        if all_links.get(i) == shortlink:
            return [i,shortlink]

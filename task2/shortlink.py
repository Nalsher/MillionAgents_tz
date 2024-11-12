
async def create_short_link(link: str) -> str:

    link = link.split("/")
    final_link = ""

    for i in range(len(link[2])):

        to_asci = ord(link[2][i])
        final_link += chr(to_asci + 1)

    return final_link

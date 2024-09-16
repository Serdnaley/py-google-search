import asyncio
import re
import aiohttp
from bs4 import BeautifulSoup

def remove_newlines(txt):
    regex = re.compile(r'[\n\r\t ]+')
    return regex.sub(' ', txt)

async def check_link(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as response:
                content = await response.text()
                soup = BeautifulSoup(content, 'html.parser')
                text = soup.get_text()

                if len(text) < 1000:
                    return None

                error_messages = [
                    "you need to enable javascript to run this app.",
                    "attention required! | cloudflare",
                    "access denied",
                    "service unavailable",
                    "error 404",
                    "error 403",
                    "error 503",
                    "404 not found",
                    "403 forbidden",
                    "503 service unavailable",
                    "500 internal server error",
                    "502 bad gateway",
                    "504 gateway timeout",
                    "522 connection timed out",
                    "524 a timeout occurred",
                    "525 origin unreachable",
                    "526 invalid ssl certificate",
                    "527 railgun error",
                    "530 origin dns error",
                    "531 origin connection error",
                    "599 network connect timeout error",
                    "529 cloudflare error",
                ]

                text_lower = text.lower()
                for error_message in error_messages:
                    if error_message in text_lower:
                        return None

                title = soup.title.string if soup.title else "No title"
                description = soup.find('meta', attrs={'name': 'description'})
                description = description['content'] if description else "No description"

                tagsToRemove = ['iframe', 'img', 'pre', 'script', 'style', 'hr', 'option', 'select', 'svg', 'video', 'input', 'nav', 'button', 'header', 'footer']

                for tag in tagsToRemove:
                    for element in soup.find_all(tag):
                        element.decompose()

                content = soup.get_text()
                content = remove_newlines(content)

                return {
                    'url': url,
                    'title': title,
                    'description': description,
                    'content': content,
                }

    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

async def process_links(links):
    tasks = [check_link(url) for url in links]
    results = await asyncio.gather(*tasks)
    return [result for result in results if result is not None]

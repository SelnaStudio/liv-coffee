import os
from PIL import Image, ImageOps

SRC = r"clientes potenciales/Liv"
DST = r"sitios/liv-coffee/assets"
os.makedirs(DST, exist_ok=True)


def save_webp(im, path, quality=80, max_w=None):
    im = ImageOps.exif_transpose(im).convert("RGB")
    if max_w and im.width > max_w:
        h = int(im.height * max_w / im.width)
        im = im.resize((max_w, h), Image.LANCZOS)
    im.save(path, "WEBP", quality=quality, method=6)
    print(path, im.size, os.path.getsize(path) // 1024, "KB")


# Verified against each source file individually (no text overlays, matches content):
photos = {
    "IMG_8472.jpg": ("hero-patio.webp", 1500, 80),      # exterior patio, plants, real signage
    "IMG_8469.jpg": ("nosotros-mesa.webp", 1200, 80),   # latte + bagel + salad, birds-eye
    "IMG_8467.jpg": ("smoothie.webp", 1000, 80),        # strawberry smoothie + plant
    "IMG_8461.jpg": ("toast-higo.webp", 1000, 80),      # toast with berries/prosciutto
    "IMG_8466.jpg": ("chilaquiles.webp", 1000, 80),     # chilaquiles roja/verde plate
    "IMG_8465.jpg": ("latte-cookie.webp", 1000, 80),    # latte + chocolate cookie
    "IMG_8462.jpg": ("huevos.webp", 1000, 78),          # huevos rojos/verdes
    "IMG_8463.jpg": ("interior-barra.webp", 1100, 80),  # barra interior, Liv wall sign
}

for src_name, (out_name, max_w, q) in photos.items():
    im = Image.open(os.path.join(SRC, src_name))
    save_webp(im, os.path.join(DST, out_name), quality=q, max_w=max_w)

print("done")

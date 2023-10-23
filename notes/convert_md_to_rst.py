import os
import m2r

os.makedirs("rst")
for filename in os.listdir("md"):
    m2r.save_to_file(
        f"rst/{filename}",
        m2r.parse_from_file(f"md/{filename}")
    )

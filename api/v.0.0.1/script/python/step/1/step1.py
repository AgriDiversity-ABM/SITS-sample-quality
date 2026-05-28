########################   IMAGEM COM PAINEL SOLAR SIMÉTRICO DE QUATRO PARTES  ########################

# import os
# import numpy as np
# import matplotlib
# matplotlib.use("Agg")

# import matplotlib.pyplot as plt
# from matplotlib.patches import Rectangle, FancyBboxPatch
# from matplotlib.transforms import Affine2D

# ARTWORK_DPI = 600

# plt.rcParams["svg.fonttype"] = "none"
# plt.rcParams["pdf.fonttype"] = 42
# plt.rcParams["ps.fonttype"] = 42


# def save_png_svg_pdf_eps(fig, png_path):
#     fig.patch.set_facecolor("white")
#     base_path, _ = os.path.splitext(png_path)

#     fig.savefig(
#         png_path,
#         bbox_inches="tight",
#         dpi=ARTWORK_DPI,
#         facecolor="white",
#         edgecolor="none",
#         format="png",
#         metadata={"Software": "Matplotlib", "dpi": str(ARTWORK_DPI)},
#         pil_kwargs={"dpi": (ARTWORK_DPI, ARTWORK_DPI), "compress_level": 1}
#     )

#     for ext in ["svg", "pdf", "eps"]:
#         fig.savefig(
#             base_path + f".{ext}",
#             bbox_inches="tight",
#             dpi=ARTWORK_DPI,
#             facecolor="white",
#             edgecolor="none",
#             format=ext
#         )


# def generate_satellite_texture(seed=7, size=420):
#     rng = np.random.default_rng(seed)

#     img = np.zeros((size, size, 3), dtype=float)
#     img[:] = np.array([35, 95, 38]) / 255

#     palette = np.array([
#         [18, 70, 30],
#         [30, 105, 42],
#         [70, 135, 55],
#         [125, 165, 55],
#         [178, 145, 75],
#         [118, 86, 45],
#         [18, 55, 72],
#         [35, 88, 120],
#     ]) / 255

#     for _ in range(160):
#         x0 = rng.integers(0, size - 40)
#         y0 = rng.integers(0, size - 40)
#         w = rng.integers(28, 95)
#         h = rng.integers(28, 95)
#         img[y0:min(size, y0 + h), x0:min(size, x0 + w)] = palette[rng.integers(0, len(palette))]

#     yy, xx = np.mgrid[0:size, 0:size]

#     for cx, cy, rx, ry in [
#         (150, 85, 33, 45),
#         (220, 175, 38, 25),
#         (75, 320, 36, 25),
#     ]:
#         mask = ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2 < 1
#         img[mask] = np.array([10, 58, 78]) / 255

#     for _ in range(11):
#         y = rng.integers(30, size - 30)
#         slope = rng.uniform(-0.18, 0.18)
#         x_start = rng.integers(0, 130)

#         for x in range(x_start, size):
#             yy_line = int(y + slope * (x - x_start))
#             if 0 <= yy_line < size:
#                 img[max(0, yy_line - 1):min(size, yy_line + 2), x] = np.array([210, 210, 185]) / 255

#     img += rng.normal(0, 0.018, img.shape)

#     return np.clip(img, 0, 1)


# def add_rotated_round_rect(
#     ax,
#     center,
#     width,
#     height,
#     angle,
#     facecolor,
#     edgecolor="black",
#     linewidth=3.0,
#     radius=0.15,
#     zorder=3
# ):
#     cx, cy = center

#     patch = FancyBboxPatch(
#         (cx - width / 2, cy - height / 2),
#         width,
#         height,
#         boxstyle=f"round,pad=0.02,rounding_size={radius}",
#         facecolor=facecolor,
#         edgecolor=edgecolor,
#         linewidth=linewidth,
#         zorder=zorder
#     )

#     patch.set_transform(
#         Affine2D().rotate_deg_around(cx, cy, angle) + ax.transData
#     )

#     ax.add_patch(patch)
#     return patch


# def draw_solar_panel(ax, center, width, height, angle):
#     cx, cy = center

#     add_rotated_round_rect(
#         ax,
#         center,
#         width,
#         height,
#         angle,
#         facecolor="#55dce8",
#         edgecolor="black",
#         linewidth=3.2,
#         radius=0.18,
#         zorder=4
#     )

#     tr = Affine2D().rotate_deg_around(cx, cy, angle) + ax.transData

#     for k in [-1, 0, 1]:
#         x = cx + k * width / 4
#         ax.plot(
#             [x, x],
#             [cy - height / 2, cy + height / 2],
#             color="black",
#             linewidth=1.7,
#             transform=tr,
#             zorder=5
#         )

#     for k in [-1, 1]:
#         y = cy + k * height / 6
#         ax.plot(
#             [cx - width / 2, cx + width / 2],
#             [y, y],
#             color="black",
#             linewidth=1.7,
#             transform=tr,
#             zorder=5
#         )


# def draw_symmetric_satellite(ax):
#     angle = -45
#     cx, cy = 8.15, 3.0

#     panel_offset = 1.72
#     arm_offset = 0.99

#     draw_solar_panel(ax, (cx - panel_offset, cy + panel_offset), 1.55, 1.55, angle)
#     draw_solar_panel(ax, (cx + panel_offset, cy + panel_offset), 1.55, 1.55, angle)
#     draw_solar_panel(ax, (cx - panel_offset, cy - panel_offset), 1.55, 1.55, angle)
#     draw_solar_panel(ax, (cx + panel_offset, cy - panel_offset), 1.55, 1.55, angle)

#     for dx, dy in [
#         (-arm_offset,  arm_offset),
#         ( arm_offset,  arm_offset),
#         (-arm_offset, -arm_offset),
#         ( arm_offset, -arm_offset),
#     ]:
#         add_rotated_round_rect(
#             ax,
#             (cx + dx, cy + dy),
#             width=0.38,
#             height=1.26,
#             angle=angle,
#             facecolor="white",
#             edgecolor="black",
#             linewidth=3.0,
#             radius=0.06,
#             zorder=5
#         )

#     add_rotated_round_rect(
#         ax,
#         (cx, cy),
#         width=1.52,
#         height=1.52,
#         angle=angle,
#         facecolor="#9fb4c7",
#         edgecolor="black",
#         linewidth=3.4,
#         radius=0.20,
#         zorder=6
#     )

#     tr = Affine2D().rotate_deg_around(cx, cy, angle) + ax.transData

#     ax.plot(
#         [cx, cx],
#         [cy - 0.76, cy + 0.76],
#         color="black",
#         linewidth=1.8,
#         transform=tr,
#         zorder=7
#     )

#     ax.plot(
#         [cx - 0.76, cx + 0.76],
#         [cy, cy],
#         color="black",
#         linewidth=1.8,
#         transform=tr,
#         zorder=7
#     )


# def create_step1_satellite_to_dataset(output_path="step_1_satellite_dataset.png"):
#     fig, ax = plt.subplots(figsize=(8.4, 4.6))

#     ax.set_xlim(0, 11.4)
#     ax.set_ylim(0, 6)
#     ax.axis("off")
#     fig.patch.set_facecolor("white")

#     texture = generate_satellite_texture()

#     ax.imshow(
#         texture,
#         extent=(0.55, 5.0, 1.0, 5.0),
#         interpolation="nearest",
#         zorder=1
#     )

#     ax.add_patch(Rectangle(
#         (0.55, 1.0),
#         4.45,
#         4.0,
#         facecolor="none",
#         edgecolor="black",
#         linewidth=2.5,
#         zorder=3
#     ))

#     draw_symmetric_satellite(ax)

#     save_png_svg_pdf_eps(fig, output_path)
#     plt.close(fig)


# if __name__ == "__main__":
#     create_step1_satellite_to_dataset("step_1_satellite_dataset.png")



########################   IMAGEM COM PAINEL SOLAR SIMÉTRICO DE DUAS PARTES, AINDA COM PEÇAS DESCONEXAS  ########################

# import os
# import numpy as np
# import matplotlib
# matplotlib.use("Agg")

# import matplotlib.pyplot as plt
# from matplotlib.patches import Rectangle, FancyBboxPatch
# from matplotlib.transforms import Affine2D

# ARTWORK_DPI = 600

# plt.rcParams["svg.fonttype"] = "none"
# plt.rcParams["pdf.fonttype"] = 42
# plt.rcParams["ps.fonttype"] = 42


# def save_png_svg_pdf_eps(fig, png_path):
#     fig.patch.set_facecolor("white")
#     base_path, _ = os.path.splitext(png_path)

#     fig.savefig(
#         png_path,
#         bbox_inches="tight",
#         dpi=ARTWORK_DPI,
#         facecolor="white",
#         edgecolor="none",
#         format="png",
#         metadata={"Software": "Matplotlib", "dpi": str(ARTWORK_DPI)},
#         pil_kwargs={"dpi": (ARTWORK_DPI, ARTWORK_DPI), "compress_level": 1}
#     )

#     for ext in ["svg", "pdf", "eps"]:
#         fig.savefig(
#             base_path + f".{ext}",
#             bbox_inches="tight",
#             dpi=ARTWORK_DPI,
#             facecolor="white",
#             edgecolor="none",
#             format=ext
#         )


# def generate_satellite_texture(seed=7, size=420):
#     rng = np.random.default_rng(seed)

#     img = np.zeros((size, size, 3), dtype=float)
#     img[:] = np.array([35, 95, 38]) / 255

#     palette = np.array([
#         [18, 70, 30],
#         [30, 105, 42],
#         [70, 135, 55],
#         [125, 165, 55],
#         [178, 145, 75],
#         [118, 86, 45],
#         [18, 55, 72],
#         [35, 88, 120],
#     ]) / 255

#     for _ in range(160):
#         x0 = rng.integers(0, size - 40)
#         y0 = rng.integers(0, size - 40)
#         w = rng.integers(28, 95)
#         h = rng.integers(28, 95)
#         img[y0:min(size, y0 + h), x0:min(size, x0 + w)] = palette[rng.integers(0, len(palette))]

#     yy, xx = np.mgrid[0:size, 0:size]

#     for cx, cy, rx, ry in [
#         (150, 85, 33, 45),
#         (220, 175, 38, 25),
#         (75, 320, 36, 25),
#     ]:
#         mask = ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2 < 1
#         img[mask] = np.array([10, 58, 78]) / 255

#     for _ in range(11):
#         y = rng.integers(30, size - 30)
#         slope = rng.uniform(-0.18, 0.18)
#         x_start = rng.integers(0, 130)

#         for x in range(x_start, size):
#             yy_line = int(y + slope * (x - x_start))
#             if 0 <= yy_line < size:
#                 img[max(0, yy_line - 1):min(size, yy_line + 2), x] = np.array([210, 210, 185]) / 255

#     img += rng.normal(0, 0.018, img.shape)

#     return np.clip(img, 0, 1)


# def add_rotated_round_rect(
#     ax,
#     center,
#     width,
#     height,
#     angle,
#     facecolor,
#     edgecolor="black",
#     linewidth=3.0,
#     radius=0.15,
#     zorder=3
# ):
#     cx, cy = center

#     patch = FancyBboxPatch(
#         (cx - width / 2, cy - height / 2),
#         width,
#         height,
#         boxstyle=f"round,pad=0.02,rounding_size={radius}",
#         facecolor=facecolor,
#         edgecolor=edgecolor,
#         linewidth=linewidth,
#         zorder=zorder
#     )

#     patch.set_transform(
#         Affine2D().rotate_deg_around(cx, cy, angle) + ax.transData
#     )

#     ax.add_patch(patch)
#     return patch


# def draw_solar_panel(ax, center, width, height, angle):
#     cx, cy = center

#     add_rotated_round_rect(
#         ax,
#         center,
#         width,
#         height,
#         angle,
#         facecolor="#55dce8",
#         edgecolor="black",
#         linewidth=3.2,
#         radius=0.18,
#         zorder=4
#     )

#     tr = Affine2D().rotate_deg_around(cx, cy, angle) + ax.transData

#     for k in [-1, 0, 1]:
#         x = cx + k * width / 4
#         ax.plot(
#             [x, x],
#             [cy - height / 2, cy + height / 2],
#             color="black",
#             linewidth=1.7,
#             transform=tr,
#             zorder=5
#         )

#     for k in [-1, 1]:
#         y = cy + k * height / 6
#         ax.plot(
#             [cx - width / 2, cx + width / 2],
#             [y, y],
#             color="black",
#             linewidth=1.7,
#             transform=tr,
#             zorder=5
#         )


# def draw_symmetric_satellite(ax):
#     angle = -45
#     cx, cy = 8.15, 3.0

#     panel_offset = 1.72
#     arm_offset = 0.99

#     # Mantidos: painel superior direito e painel inferior esquerdo.
#     # Removidos: painel superior esquerdo e painel inferior direito.
#     draw_solar_panel(ax, (cx + panel_offset, cy + panel_offset), 1.55, 1.55, angle)
#     draw_solar_panel(ax, (cx - panel_offset, cy - panel_offset), 1.55, 1.55, angle)

#     for dx, dy in [
#         (-arm_offset,  arm_offset),
#         ( arm_offset,  arm_offset),
#         (-arm_offset, -arm_offset),
#         ( arm_offset, -arm_offset),
#     ]:
#         add_rotated_round_rect(
#             ax,
#             (cx + dx, cy + dy),
#             width=0.38,
#             height=1.26,
#             angle=angle,
#             facecolor="white",
#             edgecolor="black",
#             linewidth=3.0,
#             radius=0.06,
#             zorder=5
#         )

#     add_rotated_round_rect(
#         ax,
#         (cx, cy),
#         width=1.52,
#         height=1.52,
#         angle=angle,
#         facecolor="#9fb4c7",
#         edgecolor="black",
#         linewidth=3.4,
#         radius=0.20,
#         zorder=6
#     )

#     tr = Affine2D().rotate_deg_around(cx, cy, angle) + ax.transData

#     ax.plot(
#         [cx, cx],
#         [cy - 0.76, cy + 0.76],
#         color="black",
#         linewidth=1.8,
#         transform=tr,
#         zorder=7
#     )

#     ax.plot(
#         [cx - 0.76, cx + 0.76],
#         [cy, cy],
#         color="black",
#         linewidth=1.8,
#         transform=tr,
#         zorder=7
#     )


# def create_step1_satellite_to_dataset(output_path="step_1_satellite_dataset.png"):
#     fig, ax = plt.subplots(figsize=(8.4, 4.6))

#     ax.set_xlim(0, 11.4)
#     ax.set_ylim(0, 6)
#     ax.axis("off")
#     fig.patch.set_facecolor("white")

#     texture = generate_satellite_texture()

#     ax.imshow(
#         texture,
#         extent=(0.55, 5.0, 1.0, 5.0),
#         interpolation="nearest",
#         zorder=1
#     )

#     ax.add_patch(Rectangle(
#         (0.55, 1.0),
#         4.45,
#         4.0,
#         facecolor="none",
#         edgecolor="black",
#         linewidth=2.5,
#         zorder=3
#     ))

#     draw_symmetric_satellite(ax)

#     save_png_svg_pdf_eps(fig, output_path)
#     plt.close(fig)


# if __name__ == "__main__":
#     create_step1_satellite_to_dataset("step_1_satellite_dataset.png")


########################   IMAGEM COM PAINEL SOLAR SIMÉTRICO DE DUAS PARTES  ########################


import os
import numpy as np
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from matplotlib.transforms import Affine2D

ARTWORK_DPI = 600

plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["ps.fonttype"] = 42


def save_png_svg_pdf_eps(fig, png_path):
    fig.patch.set_facecolor("white")
    base_path, _ = os.path.splitext(png_path)

    fig.savefig(
        png_path,
        bbox_inches="tight",
        dpi=ARTWORK_DPI,
        facecolor="white",
        edgecolor="none",
        format="png",
        metadata={"Software": "Matplotlib", "dpi": str(ARTWORK_DPI)},
        pil_kwargs={"dpi": (ARTWORK_DPI, ARTWORK_DPI), "compress_level": 1}
    )

    for ext in ["svg", "pdf", "eps"]:
        fig.savefig(
            base_path + f".{ext}",
            bbox_inches="tight",
            dpi=ARTWORK_DPI,
            facecolor="white",
            edgecolor="none",
            format=ext
        )


def generate_satellite_texture(seed=7, size=420):
    rng = np.random.default_rng(seed)

    img = np.zeros((size, size, 3), dtype=float)
    img[:] = np.array([35, 95, 38]) / 255

    palette = np.array([
        [18, 70, 30],
        [30, 105, 42],
        [70, 135, 55],
        [125, 165, 55],
        [178, 145, 75],
        [118, 86, 45],
        [18, 55, 72],
        [35, 88, 120],
    ]) / 255

    for _ in range(160):
        x0 = rng.integers(0, size - 40)
        y0 = rng.integers(0, size - 40)
        w = rng.integers(28, 95)
        h = rng.integers(28, 95)
        img[y0:min(size, y0 + h), x0:min(size, x0 + w)] = palette[rng.integers(0, len(palette))]

    yy, xx = np.mgrid[0:size, 0:size]

    for cx, cy, rx, ry in [
        (150, 85, 33, 45),
        (220, 175, 38, 25),
        (75, 320, 36, 25),
    ]:
        mask = ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2 < 1
        img[mask] = np.array([10, 58, 78]) / 255

    for _ in range(11):
        y = rng.integers(30, size - 30)
        slope = rng.uniform(-0.18, 0.18)
        x_start = rng.integers(0, 130)

        for x in range(x_start, size):
            yy_line = int(y + slope * (x - x_start))
            if 0 <= yy_line < size:
                img[max(0, yy_line - 1):min(size, yy_line + 2), x] = np.array([210, 210, 185]) / 255

    img += rng.normal(0, 0.018, img.shape)

    return np.clip(img, 0, 1)


def add_rotated_round_rect(
    ax,
    center,
    width,
    height,
    angle,
    facecolor,
    edgecolor="black",
    linewidth=3.0,
    radius=0.15,
    zorder=3
):
    cx, cy = center

    patch = FancyBboxPatch(
        (cx - width / 2, cy - height / 2),
        width,
        height,
        boxstyle=f"round,pad=0.02,rounding_size={radius}",
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=linewidth,
        zorder=zorder
    )

    patch.set_transform(
        Affine2D().rotate_deg_around(cx, cy, angle) + ax.transData
    )

    ax.add_patch(patch)
    return patch


def draw_solar_panel(ax, center, width, height, angle):
    cx, cy = center

    add_rotated_round_rect(
        ax,
        center,
        width,
        height,
        angle,
        facecolor="#55dce8",
        edgecolor="black",
        linewidth=3.2,
        radius=0.18,
        zorder=4
    )

    tr = Affine2D().rotate_deg_around(cx, cy, angle) + ax.transData

    for k in [-1, 0, 1]:
        x = cx + k * width / 4
        ax.plot(
            [x, x],
            [cy - height / 2, cy + height / 2],
            color="black",
            linewidth=1.7,
            transform=tr,
            zorder=5
        )

    for k in [-1, 1]:
        y = cy + k * height / 6
        ax.plot(
            [cx - width / 2, cx + width / 2],
            [y, y],
            color="black",
            linewidth=1.7,
            transform=tr,
            zorder=5
        )


def draw_symmetric_satellite(ax):
    angle = -45
    cx, cy = 8.15, 3.0

    panel_offset = 1.72
    arm_offset = 0.99

    # Mantidos: painel superior direito e painel inferior esquerdo.
    draw_solar_panel(ax, (cx + panel_offset, cy + panel_offset), 1.55, 1.55, angle)
    draw_solar_panel(ax, (cx - panel_offset, cy - panel_offset), 1.55, 1.55, angle)

    # Mantidos: apenas os conectores que ligam os painéis preservados ao corpo central.
    # Removidos: conector superior esquerdo e conector inferior direito.
    for dx, dy in [
        ( arm_offset,  arm_offset),
        (-arm_offset, -arm_offset),
    ]:
        add_rotated_round_rect(
            ax,
            (cx + dx, cy + dy),
            width=0.38,
            height=1.26,
            angle=angle,
            facecolor="white",
            edgecolor="black",
            linewidth=3.0,
            radius=0.06,
            zorder=5
        )

    add_rotated_round_rect(
        ax,
        (cx, cy),
        width=1.52,
        height=1.52,
        angle=angle,
        facecolor="#9fb4c7",
        edgecolor="black",
        linewidth=3.4,
        radius=0.20,
        zorder=6
    )

    tr = Affine2D().rotate_deg_around(cx, cy, angle) + ax.transData

    ax.plot(
        [cx, cx],
        [cy - 0.76, cy + 0.76],
        color="black",
        linewidth=1.8,
        transform=tr,
        zorder=7
    )

    ax.plot(
        [cx - 0.76, cx + 0.76],
        [cy, cy],
        color="black",
        linewidth=1.8,
        transform=tr,
        zorder=7
    )


def create_step1_satellite_to_dataset(output_path="step_1_satellite_dataset.png"):
    fig, ax = plt.subplots(figsize=(8.4, 4.6))

    ax.set_xlim(0, 11.4)
    ax.set_ylim(0, 6)
    ax.axis("off")
    fig.patch.set_facecolor("white")

    texture = generate_satellite_texture()

    ax.imshow(
        texture,
        extent=(0.55, 5.0, 1.0, 5.0),
        interpolation="nearest",
        zorder=1
    )

    ax.add_patch(Rectangle(
        (0.55, 1.0),
        4.45,
        4.0,
        facecolor="none",
        edgecolor="black",
        linewidth=2.5,
        zorder=3
    ))

    draw_symmetric_satellite(ax)

    save_png_svg_pdf_eps(fig, output_path)
    plt.close(fig)


if __name__ == "__main__":
    create_step1_satellite_to_dataset("step_1_satellite_dataset.png")

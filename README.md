# 🧊 Mesh Maker - Blender Add-on

A simple Blender add-on that lets you **create and manage multiple cubes** from the 3D View sidebar panel.  
Built using Python and the Blender API.

## ✨ Features

- UI panel in the **3D Viewport > Sidebar > Mesh Maker** tab
- Input field to set the number of cubes
- Button to **generate N cubes** in a grid
- Automatically places cubes into a **custom collection** named `GeneratedCubes`
- Button to **delete selected objects**
- Basic error handling (e.g., cube count limit, no selection warnings)

## 📂 Installation

1. Download or clone this repository.
2. Open Blender.
3. Go to **Edit > Preferences > Add-ons > Install**.
4. Select the `.zip` file (or `.py` file) of the add-on.
5. Enable the add-on by checking the box.
6. Find it under **View3D > Sidebar > Mesh Maker**.

## ⚙️ How to Use

1. Go to the **Mesh Maker** tab in the sidebar (press `N` in the 3D Viewport if it's not visible).
2. Enter the number of cubes you want to create (max 50).
3. Click **"Create Cubes"** to generate them in a grid.
4. Select any objects and click **"Delete Selected"** to remove them from the scene.

## 🧠 How It Works

- Uses `bpy.ops.mesh.primitive_cube_add` to create cubes.
- Adds each cube to a custom collection called `GeneratedCubes`.
- Optionally unlinks cubes from the default Scene Collection.
- Includes a property (`cube_count`) attached to the Blender Scene for user input.

## 🚫 Limitations

- Maximum of 50 cubes at a time (for performance).
- Only works with cubes (for now 😉).

## 📜 License

MIT License — free to use, modify, and share.

## 🙋‍♀️ Author

Developed by **Radhika Khatter**  
Feel free to connect on [Twitter](https://twitter.com/) or drop feedback!

---

🧪 *More features coming soon — stay tuned!*

import omni.ext
import omni.ui as ui
import omni.kit.commands

import functools


# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print("[eg.cube] some_public_function was called with x: ", x)
    return x ** x


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class EgCubeExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[eg.cube] eg cube startup")

        self._count = 0

        self._window = ui.Window("Spawn a Cube", width=300, height=300)
        with self._window.frame:
            with ui.VStack():
                label = ui.Label("")

                def on_click(prim_type):
                    print('making a cube!')

                    # # omniverse command style
                    # results = omni.kit.commands.execute('CreatePrimWithDefaultXform',
                    #                                     prim_type=prim_type,
                    #                                     attributes={'size': 100.0,
                    #                                                 'extent': [(-50.0, -50.0, -50.0), (50.0, 50.0, 50.0)]})

                    # # usd style
                    # from pxr import UsdGeom
                    # stage = omni.usd.get_context().get_stage()
                    # prim = UsdGeom.Cube.Define(stage, '/World/cube')

                    omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
                                              prim_type=prim_type)

                prim_type_list = ['Cube', 'Cone', 'Cylinder', 'Disk', 'Plane', 'Sphere', 'Torus']
                # with ui.HStack():
                for prim_type in prim_type_list:
                    fn = functools.partial(on_click, prim_type)
                    ui.Button("Spawn {}".format(prim_type), clicked_fn=fn)
                    # ui.Button("Spawn cone", clicked_fn=lambda: on_click('Cone'))

    def on_shutdown(self):
        print("[eg.cube] eg cube shutdown")

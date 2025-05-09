"""

RenderPipeline

Copyright (c) 2014-2016 tobspr <tobias.springer1@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

from metaurban.render_pipeline.rpcore.pluginbase.base_plugin import BasePlugin

from .ssr_stage import SSRStage


class Plugin(BasePlugin):

    name = "Screen Space Reflections"
    author = "tobspr <tobias.springer1@gmail.com>"
    description = (
        "This plugin adds support for stochastik screen space reflections "
        "and is still very experimental!"
    )
    version = "beta (!)"

    def on_stage_setup(self):
        self.ssr_stage = self.create_stage(SSRStage)

        if self.is_plugin_enabled("color_correction"):
            self.ssr_stage.required_pipes.append("FuturePipe::Exposure")

    def reload_shaders(self):
        BasePlugin.reload_shaders(self)

        # Also update the ambient stage
        self._pipeline.stage_mgr.get_stage("AmbientStage").reload_shaders()

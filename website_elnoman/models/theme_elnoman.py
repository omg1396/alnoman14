from odoo import models


class themeElnoman(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_elnoman_post_copy(self, mod):
        # self.disable_view('website_theme_install.customize_modal')
        self.disable_view('website.header_visibility_standard')


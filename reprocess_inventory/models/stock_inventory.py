from odoo import api, fields, models


class Inventory(models.Model):
    _inherit = 'stock.inventory'

    def reset_to_progress(self):
        for inventory in self:
            if inventory.move_ids:
                for move in inventory.move_ids:
                    rev_move = move.copy()
                    rev_move.location_id = move.location_dest_id.id
                    rev_move.location_dest_id = move.location_id.id
                    rev_move._action_done()
            inventory.move_ids = [(6, 0, [])]
            inventory.state = 'confirm'

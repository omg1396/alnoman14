# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartnerSequence(models.Model):
    _name = 'res.partner.seqeunce'
    _description = 'Res Partner Sequence'
    partner_id = fields.Many2one('res.partner', 'Partner')
    sequence = fields.Char('Sequence')


class ResPartner(models.Model):
    _inherit = 'res.partner'
    # generate sequences as default.
    # as the field is set as index, then it should be unique,
    # so we need to remove the reference on archiving!
    ref = fields.Char(string='Reference', index=True,
                      default=lambda self: self.get_default_sequence(), copy=False)

    def get_default_sequence(self):
        """check the archived sequences, if there is one returned and delete the archived sequenc,
        if there is no gap, return new sequence

        Returns:
            char: sequence
        """
        gapped_sequences = self.env['res.partner.seqeunce'].sudo().search([])
        if gapped_sequences:
            sequence = gapped_sequences[0].sudo().sequence
            gapped_sequences[0].sudo().unlink()
            return sequence
        else:
            # we don't need to consume the sequence on the default. we need to consume it after creation.
            seq_id = self.env['ir.sequence'].sudo().search(
                [('code', '=', 'res.partner.reference')], limit=1)[0]
            return seq_id.get_next_char(seq_id.number_next_actual)

    # should be implemented?
    def _resequence_reference(self):
        """regerenate sequences for partners
        """
        for partner in self:
            partner.ref = self.env['ir.sequence'].next_by_code(
                'res.partner.reference')

    # remomve the reference before archiving
    def action_archive(self):
        for partner in self.filtered(lambda p: p.ref):
            self.env['res.partner.seqeunce'].sudo().create(
                {
                    'partner_id': partner.id,
                    'sequence': partner.ref
                }
            )
        self.ref = ''
        return super(ResPartner, self).action_archive()

    def action_unarchive(self):
        for partner in self:
            partner.ref = partner.get_default_sequence()
        return super(ResPartner, self).action_unarchive()

    @api.model
    def create(self, vals):
        partners = super(ResPartner, self).create(vals)
        # consume sequences after creation
        for partner in partners:
            self.env['ir.sequence'].next_by_code(
                'res.partner.reference')
        return partners

    def generate_references(self):
        """generate sequences for partners.
        """
        partners_without_reference = self.sudo().filtered(
            lambda p: not p.ref).sorted(lambda partner: partner.id)
        for partner_without_sequence in partners_without_reference:
            partner_without_sequence.ref = self.env['ir.sequence'].next_by_code(
                'res.partner.reference')

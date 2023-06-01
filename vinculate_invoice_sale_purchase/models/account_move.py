from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'
    purchase_vinculate_jz = fields.Many2one('purchase.order',string="Purchase to Related")

    def vinculate_purchase_jz(self):
        for line in self.invoice_line_ids:
            for purchaseline in self.purchase_vinculate_jz.order_line:
                if purchaseline.product_id == line.product_id:
                    #raise ValueError('kkk')
                    line.sudo().write({
                        'purchase_line_id': purchaseline.id
                    })

    def des_vinculate_purchase_jz(self):
        for line in self.invoice_line_ids:
            for purchaseline in self.purchase_vinculate_jz.order_line:
                if purchaseline.product_id == line.product_id:
                    line.sudo().write({
                        'purchase_line_id': False
                    })
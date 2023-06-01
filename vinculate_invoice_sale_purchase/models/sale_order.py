from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    invoice_vinculate_jz = fields.Many2one('account.move',string="Invoice to Related")

    def vinculate_sale_jz(self):
        for line in self.order_line:
            for invoiceline in self.invoice_vinculate_jz.invoice_line_ids:
                if invoiceline.product_id == line.product_id:
                    line.invoice_lines = [(4,invoiceline.id)]

    def des_vinculate_sale_jz(self):
        for line in self.order_line:
            for invoiceline in self.invoice_vinculate_jz.invoice_line_ids:
                if invoiceline.product_id == line.product_id:
                    line.invoice_lines = [(3,invoiceline.id)]

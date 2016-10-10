# -*- encoding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################

from openerp import models, fields, api,  _
from openerp.exceptions import Warning, ValidationError, except_orm


class RawMaterial(models.Model):
    _name= 'mrp.raw.material'
    _description= 'Dato y caracterisiticas técnicas para producción - Materia Prima'

    ord_id = fields.Many2one('mrp.production', 'Orden de Produccion',required=1, ondelete='cascade')
    name= fields.Selection([('bond', 'Bond'), ('termico', 'Térmico'), ('q-cb', 'Q - CB'),('q-cf','Q-CF'),
        ('q-cfb', 'Q-CFB')],
        string='Papel')
    kg = fields.Float(
        string='KG',digits=(6,2),required=False)
    paper_processing = fields.Float(
        string='Papel Procesado',digits=(6,2),required=False)
    total_load = fields.Float(
        string='Carga Total',digits=(6,2),required=False)
    coil_width = fields.Float(
        string='Ancho de Bobina',digits=(6,2),required=False)
    high_form = fields.Float(
        string='Alto de Formulario',digits=(6,2),required=False)
    armed = fields.Float(string='Armado',digits=(6,2),required=False)
# -*- encoding: utf-8 -*-
###############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from osv import osv, fields


class hr_experience(osv.osv):
    _name = 'hr.experience'
    _columns = {
        'name': fields.char('Name', size=64, required=True, translate=True),
        'employee_id': fields.many2one('hr.employee', 'Employee', required=True),
        'category': fields.selection((('professional', 'Professional'),
                                     ('academic', 'Academic'),
                                     ('certification', 'Certification')),
                                     'Category', required=True),
        'start_date': fields.date('Start date'),
        'end_date': fields.date('End date'),
        'description': fields.text('Description', translate=True),
        'partner_id': fields.many2one('res.partner', 'Partner', help="Employer, School, University, Certification Authority"),
        'location': fields.char('Location', size=64, translate=True),
        'diploma': fields.char('Diploma', size=64, translate=True),
        'study_field': fields.char('Field of study', size=64, translate=True),
        'result': fields.char('Result', size=64, translate=True),
        'activities': fields.text('Activities and associations', translate=True),
        'certification': fields.char('Certification Number', size=64),
        'expire': fields.boolean('Expire'),
    }

    _defaults = {
        'category': 'professional',
        'expire': True,
    }
hr_experience()


class hr_employee(osv.osv):
    _inherit = 'hr.employee'
    _columns = {
        'experience_ids': fields.one2many('hr.experience', 'employee_id', 'Experiences'),
    }
hr_employee()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

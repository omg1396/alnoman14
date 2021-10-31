from werkzeug.exceptions import NotFound

from odoo import http, models, fields, _
from odoo.http import request
from odoo.addons.website.controllers.main import Website
from datetime import timezone, datetime, timedelta, time


class CustomerReviews(http.Controller):
    @http.route(['/reviews', '/reviews/page/<int:page>'], type='http', auth="public",
                website=True)
    def Customer_reviews_page(self, page=0, **kw):
        CustomerReview = request.env['customer.review'].sudo().search([])
        total = CustomerReview.sudo().search_count([])
        pager = request.website.pager(
            url='/reviews',
            total=total,
            page=page,
            step=10,
        )
        offset = pager['offset']
        customer_review = CustomerReview[offset: offset + 10]
        data = {'customer_review': customer_review, 'pager': pager}
        return http.request.render('website_elnoman.elnoman_reviews_page', data)


class Website(Website):
    @http.route(auth='public')
    def index(self, page=0, **kw):
        """function home page"""
        super(Website, self).index(**kw)
        CustomerReview = request.env['customer.review'].sudo().search([])
        total = CustomerReview.sudo().search_count([])
        pager = request.website.pager(
            url='/',
            total=total,
            page=page,
            step=10,
        )
        offset = pager['offset']
        customer_review = CustomerReview[offset: offset + 10]
        data = {'customer_review': customer_review, 'pager': pager}
        return http.request.render('website_elnoman.elnoman_home_page', data)


class LatestProducts(http.Controller):
    @http.route(['/latest_product', '/latest_product/page/<int:page>'], type='http', auth="public",
                website=True)
    def Customer_reviews_page(self, page=0, **post):
        LatestProducts = request.env['product.template'].sudo().search([('latest_product', '=', True)])
        total = len(LatestProducts.ids)
        pager = request.website.pager(
            url='/latest_product',
            total=total,
            page=page,
            step=12,
            scope=7,
            url_args=post
        )
        offset = pager['offset']
        latest_product = LatestProducts[offset: offset + 12]
        data = {'latest_product': latest_product, 'pager': pager,
                'search_count': total,
                'ppg': 12,
                'ppr': 4}
        return http.request.render('website_elnoman.elnoman_latest_product_page', data)

    @http.route([
        '''/latest_product/<model("product.template"):latest>''',
    ], type='http', auth="public", website=True, sitemap=True)
    def customer_reviews_page_details(self, latest, enable_editor=None, **post):
        if not latest:
            raise NotFound()
        return http.request.render('website_elnoman.elnoman_latest_product_details_page',
                                   {'record': latest})

from front_controllers.base_fc import current_date
from views import IndexView, AboutView, PricingView, ContactUsView, CreateCategoryView

routes = {
    '/': IndexView(),
    '/about/': AboutView(),
    '/contact_us/': ContactUsView(),
    '/pricing/': PricingView(),
    '/create_category/': CreateCategoryView(),
}

fronts = (current_date, )

from front_controllers.base_fc import current_date
from views import IndexView, AboutView, PricingView, ContactUsView

routes = {
    '/': IndexView(),
    '/about/': AboutView(),
    '/contact_us/': ContactUsView(),
    '/pricing/': PricingView(),
}

fronts = (current_date, )

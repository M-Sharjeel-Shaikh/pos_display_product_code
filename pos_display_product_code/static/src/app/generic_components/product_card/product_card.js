/* @odoo-module */

import { useEffect, useState } from "@odoo/owl";
import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card";
import { patch } from "@web/core/utils/patch";

patch(ProductCard.prototype, {
    setup() {
        super.setup(...arguments);
        this.default_code = useState({ value: this.props.product.default_code });
        this.display_default_code = posmodel.env.services.pos.config.display_default_code || false;
    },
});

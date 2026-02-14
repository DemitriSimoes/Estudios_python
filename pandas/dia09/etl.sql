SELECT seller_id,
        sum(price),
        count(distinct order_id)
FROM tb_order_items

GROUP BY seller_id
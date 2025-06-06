SELECT
    sub.global_key,
    sub.label,
    sub.URL,
    sub.building_key
FROM
    (
        SELECT
            t.global_key,
            t.building_key,
            img.type AS label,
            img.thumbnail_url AS URL,
            ROW_NUMBER() OVER (PARTITION BY img.type, t.building_key ORDER BY img.thumbnail_url, t.global_key) AS rn_building_key,
            ROW_NUMBER() OVER (PARTITION BY img.type ORDER BY t.building_key, img.thumbnail_url, t.global_key) AS rn_total
        FROM
            `lake_site.smocca_solr_group_with_images` AS t,
            UNNEST(t.images) AS img
        WHERE
            t.exported_at = "2025-06-01"
            AND r_only_flag = true
    ) AS sub
WHERE
    sub.rn_building_key = 1
    AND (
        CASE 
            WHEN sub.label = '9' THEN sub.rn_total <= 3000   -- other
            WHEN sub.label = '10' THEN sub.rn_total <= 2000  -- doorway
            WHEN sub.label = '15' THEN sub.rn_total <= 2000  -- bathroom
            ELSE sub.rn_total <= 1500   -- デフォルトは1500枚分のURLを収集
        END
    )
ORDER BY
    sub.label, sub.building_key;
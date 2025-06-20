WITH ranked_images AS (
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
    t.exported_at = "2025-06-09"
    AND t.apaman_only_flag = True
)

SELECT
  global_key,
  label,
  URL,
  building_key,
FROM
  ranked_images
WHERE
  rn_building_key = 1
  AND label in ("3", "5","9", "15")
ORDER BY
  label, building_key;
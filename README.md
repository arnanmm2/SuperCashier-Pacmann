
# Supermarket Self-Service Cashier System

## Background

Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia. Andi memiliki rencana untuk melakukan perbaikan proses bisnis dengan menciptakan sistem kasir self-service di supermarket miliknya. Ini memungkinkan pelanggan untuk memasukkan item yang ingin dibeli, jumlah item, dan harga item secara langsung. Selain itu, sistem ini juga memungkinkan pelanggan yang tidak berada di kota tersebut untuk melakukan pembelian. Namun, Andi menghadapi masalah karena ia membutuhkan programmer untuk me...

## Requirements

1. Customer membuat ID transaksi dengan menciptakan objek dari kelas (contoh: `trnsct_123 = Transaction()`).
2. Customer memasukkan nama item, jumlah item, dan harga barang dengan metode `add_item([<nama item>, <jumlah item>, <harga item>])`.
3. Customer dapat memperbarui detail item jika terjadi kesalahan dalam input menggunakan metode:
   - `update_item_name(<nama item>, <nama item baru>)`
   - `update_item_qty(<nama item>, <jumlah item baru>)`
   - `update_item_price(<nama item>, <harga item baru>)`
4. Jika customer batal membeli, mereka dapat menghapus item atau mereset transaksi menggunakan metode:
   - `delete_item(<nama item>)`
   - `reset_transaction()`
5. Sebelum menyelesaikan transaksi, customer dapat memeriksa pesanan mereka menggunakan metode `check_order()` yang mencetak detail transaksi dan pesan konfirmasi atau peringatan kesalahan.
6. Setelah memeriksa, customer dapat menghitung total belanja dengan metode `total_price()` yang juga menerapkan diskon berdasarkan total belanja.

## Modules

1. **random**: Digunakan untuk menghasilkan ID transaksi acak.
2. **datetime**: Digunakan untuk mendapatkan tanggal dan waktu transaksi saat ini.
3. **tabulate**: Digunakan untuk mencetak faktur dalam format tabel yang rapi.
4. **numpy**: Digunakan untuk operasi numerik (meskipun tampaknya tidak digunakan dalam kode ini).
## Flowchart
```xml
<mxfile host="app.diagrams.net" modified="2023-09-09T04:52:03.936Z" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69" etag="KX_YsWWFyWwaZUSuSYXH" version="21.7.3" type="device">
<diagram name="Page-1" id="TTu5Kb3rv_GLVrESf8Uf">
<mxGraphModel dx="3202" dy="1369" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
<root>
<mxCell id="0"/>
<mxCell id="1" parent="0"/>
<mxCell id="am94PVR-MiZx4M0_MHR_-18" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="B-QTdc27rYNYUVgxviTm-2" target="B-QTdc27rYNYUVgxviTm-3">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="B-QTdc27rYNYUVgxviTm-2" value="Mulai" style="rounded=1;whiteSpace=wrap;html=1;" parent="1" vertex="1">
<mxGeometry x="260" y="110" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-17" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="B-QTdc27rYNYUVgxviTm-3" target="B-QTdc27rYNYUVgxviTm-4">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="B-QTdc27rYNYUVgxviTm-3" value="Membuat Transaction ID" style="rounded=0;whiteSpace=wrap;html=1;" parent="1" vertex="1">
<mxGeometry x="235" y="230" width="170" height="60" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-16" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="B-QTdc27rYNYUVgxviTm-4" target="am94PVR-MiZx4M0_MHR_-9">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="B-QTdc27rYNYUVgxviTm-4" value="Add item<br>Inpurt nama item, kuantitas, dan harga" style="rounded=0;whiteSpace=wrap;html=1;" parent="1" vertex="1">
<mxGeometry x="220" y="330" width="200" height="60" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-55" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-1" target="am94PVR-MiZx4M0_MHR_-2">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-1" value="Cek item apakah akan di update atau delete item&nbsp;" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="-10" y="870" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-49" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-2" target="am94PVR-MiZx4M0_MHR_-5">
<mxGeometry relative="1" as="geometry">
<Array as="points">
<mxPoint x="160" y="1015"/>
<mxPoint x="160" y="1355"/>
</Array>
</mxGeometry>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-52" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-2" target="am94PVR-MiZx4M0_MHR_-3">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-2" value="update detail item ?" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="-20" y="970" width="140" height="90" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-53" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-3" target="am94PVR-MiZx4M0_MHR_-4">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-3" value="Pilih update<br>-nama<br>-kuantitas<br>-harga" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="-10" y="1100" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-54" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-4" target="am94PVR-MiZx4M0_MHR_-5">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-4" value="update itme berdasarkan pilihan" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="-10" y="1200" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-50" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-5" target="am94PVR-MiZx4M0_MHR_-7">
<mxGeometry relative="1" as="geometry">
<Array as="points">
<mxPoint x="-60" y="1355"/>
<mxPoint x="-60" y="1580"/>
</Array>
</mxGeometry>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-56" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-5" target="am94PVR-MiZx4M0_MHR_-6">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-5" value="delete item ?" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="-15" y="1310" width="130" height="90" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-57" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-6" target="am94PVR-MiZx4M0_MHR_-7">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-6" value="delete item dari list" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="-10" y="1440" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-51" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-7" target="am94PVR-MiZx4M0_MHR_-8">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-58" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-7" target="am94PVR-MiZx4M0_MHR_-22">
<mxGeometry relative="1" as="geometry">
<Array as="points">
<mxPoint x="240" y="1580"/>
<mxPoint x="240" y="890"/>
</Array>
</mxGeometry>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-7" value="Reset transaksi ?" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="10" y="1540" width="80" height="80" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-59" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-8">
<mxGeometry relative="1" as="geometry">
<mxPoint x="270" y="1960" as="targetPoint"/>
<Array as="points">
<mxPoint x="50" y="1960"/>
</Array>
</mxGeometry>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-8" value="Clear semua item dari list transaksi" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="-10" y="1660" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-15" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-9" target="am94PVR-MiZx4M0_MHR_-10">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-9" value="Validasi input<br>Nama harus dalam Str<br>kuantitas harus int<br>harga harus int atau float" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="225" y="430" width="190" height="60" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-13" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-10" target="am94PVR-MiZx4M0_MHR_-11">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-21" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-10" target="am94PVR-MiZx4M0_MHR_-12">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-10" value="Apakah terdapat error saat input ?" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="197.5" y="530" width="245" height="80" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-46" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-11" target="B-QTdc27rYNYUVgxviTm-4">
<mxGeometry relative="1" as="geometry">
<Array as="points">
<mxPoint x="-60" y="667"/>
<mxPoint x="-60" y="360"/>
</Array>
</mxGeometry>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-11" value="Pemberitahuan error&nbsp; input" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry y="637" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-19" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-12" target="am94PVR-MiZx4M0_MHR_-1">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-32" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-12" target="am94PVR-MiZx4M0_MHR_-22">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-12" value="Lanjut ke porses selanjutnya&nbsp;" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="510" y="750" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-33" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-22" target="am94PVR-MiZx4M0_MHR_-23">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-22" value="Check order apakah&nbsp; semua order sudah terinput dengan baik" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="510" y="860" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-35" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-23" target="am94PVR-MiZx4M0_MHR_-25">
<mxGeometry relative="1" as="geometry">
<Array as="points">
<mxPoint x="830" y="1005"/>
<mxPoint x="830" y="1090"/>
</Array>
</mxGeometry>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-47" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-23" target="am94PVR-MiZx4M0_MHR_-24">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-23" value="Terdapat error pada order ?" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="485" y="960" width="170" height="90" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-73" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.576;entryY=0.017;entryDx=0;entryDy=0;entryPerimeter=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-24">
<mxGeometry relative="1" as="geometry">
<mxPoint x="339.1199999999999" y="1931.0200000000004" as="targetPoint"/>
</mxGeometry>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-24" value="Pemberitahuan error" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="280" y="1090" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-36" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-25" target="am94PVR-MiZx4M0_MHR_-26">
<mxGeometry relative="1" as="geometry">
<Array as="points">
<mxPoint x="830" y="1250"/>
</Array>
</mxGeometry>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-25" value="Konfirmasi order sudah benar" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="770" y="1090" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-37" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-26" target="am94PVR-MiZx4M0_MHR_-27">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-26" value="Hitung total harga" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="510" y="1220" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-38" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-27" target="am94PVR-MiZx4M0_MHR_-28">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-40" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-27" target="am94PVR-MiZx4M0_MHR_-29">
<mxGeometry relative="1" as="geometry">
<Array as="points">
<mxPoint x="730" y="1380"/>
<mxPoint x="730" y="1670"/>
</Array>
</mxGeometry>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-27" value="Apakah mendapat diskon ?" style="rhombus;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="477.5" y="1340" width="185" height="80" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-42" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-28" target="am94PVR-MiZx4M0_MHR_-29">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-28" value="Apply diskon berdasarkan total harga" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="510" y="1480" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-43" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-29" target="am94PVR-MiZx4M0_MHR_-30">
<mxGeometry relative="1" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-29" value="Tunjukkan total harga final&nbsp;" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="510" y="1640" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-60" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="am94PVR-MiZx4M0_MHR_-30">
<mxGeometry relative="1" as="geometry">
<mxPoint x="390" y="1960" as="targetPoint"/>
<Array as="points">
<mxPoint x="570" y="1960"/>
</Array>
</mxGeometry>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-30" value="Print Invoice" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="510" y="1780" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-61" value="YA" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
<mxGeometry x="50" y="1060" width="50" height="30" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-62" value="TIDAK" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
<mxGeometry x="115" y="980" width="50" height="30" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-65" value="TIDAK" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
<mxGeometry x="720" y="980" width="50" height="30" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-66" value="YA" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
<mxGeometry x="405" y="980" width="50" height="30" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-67" value="YA" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
<mxGeometry x="40" y="1400" width="50" height="30" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-68" value="TIDAK" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
<mxGeometry x="-60" y="1330" width="50" height="30" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-69" value="TIDAK" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
<mxGeometry x="100" y="1550" width="50" height="30" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-70" value="YA" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
<mxGeometry x="40" y="1630" width="50" height="30" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-71" value="TIDAK" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
<mxGeometry x="670" y="1350" width="50" height="30" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-72" value="YA" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
<mxGeometry x="520" y="1430" width="50" height="30" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-74" value="SELESAI" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
<mxGeometry x="270" y="1930" width="120" height="60" as="geometry"/>
</mxCell>
<mxCell id="am94PVR-MiZx4M0_MHR_-75" value="Input lagi" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;rotation=-90;" vertex="1" parent="1">
<mxGeometry x="-110" y="520" width="60" height="30" as="geometry"/>
</mxCell>
</root>
</mxGraphModel>
</diagram>
</mxfile>
```
## Cara pakai
1. Pertama user membuka file Supercashier.py
2. Setelah program sudah di buka, akan terdapat petunjuk penggunaan.
3. User dapat memilih dari angka 1-6 untuk memilih fitur yang ada pada program ini
   
## Functions

### validate_name(name)
```python
def validate_name(name):
    # Validasi nama item, nama item harus berupa string
    if not isinstance(name, str):
        raise ValueError("nama item harus string")
```
Fungsi ini memvalidasi bahwa nama item yang dimasukkan adalah string. Jika tidak, ia akan memunculkan ValueError.

### validate_qty(qty)
```python
def validate_qty(qty):
    # validasi kuantitas item, harus lebih besar dari 0
    if not isinstance(qty, (int, float)) or qty <= 0:
        raise ValueError("Kuantitas item harus lebih besar daripada 0")
```
Fungsi ini memvalidasi bahwa kuantitas item yang dimasukkan adalah angka yang lebih besar dari 0. Jika tidak, ia akan memunculkan ValueError.

### validate_price(price)
```python
def validate_price(price):
    # validasi harga, harga tidak boleh minus
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("Harga item tidak boleh negatif")
```
Fungsi ini memvalidasi bahwa harga item yang dimasukkan adalah angka non-negatif. Jika tidak, ia akan memunculkan ValueError.

## Class: Transaction

Kelas ini mengatur seluruh operasi yang berhubungan dengan transaksi individual.

```python
class Transaction:
    def __init__(self):
        self.transaction_id = f"TRX-{random.randint(1000, 9999)}"
        self.transaction_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.items = {}
```

### __init__(self) - Requirement

Metode konstruktor ini menginisialisasi objek transaksi baru dengan ID transaksi acak dan tanggal transaksi saat ini, serta mendefinisikan dictionary kosong untuk menyimpan item-item yang akan dibeli.

### add_item(self, item_details) - Requirement

```python
def add_item(self, item_details):
    try:
        name, qty, price = item_details
        validate_name(name)
        validate_qty(qty)
        validate_price(price)
        self.items[name] = {'quantity': qty, 'price': price}
    except ValueError as e:
        print(f"Kesalahan saat menambahkan item: {e}")
```

Metode ini memungkinkan pelanggan untuk menambahkan item ke transaksi. Item-details harus berupa list yang berisi nama item (string), kuantitas (angka positif), dan harga (angka non-negatif). Jika terjadi kesalahan validasi, akan mencetak pesan kesalahan.

### update_item_name(self, old_name, new_name) - Requirement

```python
def update_item_name(self, old_name, new_name):
    try:
        validate_name(new_name)
        if old_name in self.items:
            self.items[new_name] = self.items.pop(old_name)
        else:
            raise ValueError("Item tidak ditemukan dalam transaksi")
    except ValueError as e:
        print(f"Kesalahan saat memperbarui nama item: {e}")
```

Metode ini memungkinkan pelanggan untuk memperbarui nama item dalam transaksi. Ia memvalidasi nama baru dan memeriksa apakah item lama ada dalam transaksi sebelum memperbaruinya. Jika terjadi kesalahan, ia akan mencetak pesan kesalahan.

### update_item_qty(self, name, new_qty) - Requirement

```python
def update_item_qty(self, name, new_qty):
    try:
        validate_qty(new_qty)
        if name in self.items:
            self.items[name]['quantity'] = new_qty
        else:
            raise ValueError("Item tidak ditemukan dalam transaksi")
    except ValueError as e:
        print(f"Kesalahan saat memperbarui kuantitas item: {e}")
```

Metode ini memungkinkan pelanggan untuk memperbarui kuantitas item dalam transaksi. Ia memvalidasi kuantitas baru dan memeriksa apakah item ada dalam transaksi sebelum memperbaruinya. Jika terjadi kesalahan, ia akan mencetak pesan kesalahan.

### update_item_price(self, name, new_price) - Requirement

```python
def update_item_price(self, name, new_price):
    try:
        validate_price(new_price)
        if name in self.items:
            self.items[name]['price'] = new_price
        else:
            raise ValueError("Item tidak ditemukan dalam transaksi")
    except ValueError as e:
        print(f"Kesalahan saat memperbarui harga item: {e}")
```

Metode ini memungkinkan pelanggan untuk memperbarui harga item dalam transaksi. Ia memvalidasi harga baru dan memeriksa apakah item ada dalam transaksi sebelum memperbaruinya. Jika terjadi kesalahan, ia akan mencetak pesan kesalahan.

### delete_item(self, name) - Requirement

```python
def delete_item(self, name):
    try:
        validate_name(name)
        if name in self.items:
            del self.items[name]
        else:
            raise ValueError("Item tidak ditemukan dalam transaksi")
    except ValueError as e:
        print(f"Kesalahan saat menghapus item: {e}")
```

Metode ini memungkinkan pelanggan untuk menghapus item dari transaksi. Ia memvalidasi nama item dan memeriksa apakah item ada dalam transaksi sebelum menghapusnya. Jika terjadi kesalahan, ia akan mencetak pesan kesalahan.

### reset_transaction(self) - Requirement

```python
def reset_transaction(self):
    self.items = {}
```

Metode ini mereset transaksi dengan menghapus semua item dari transaksi saat ini.

### check_order(self) - Requirement

```python
def check_order(self):
    if all(self.items[item].get('quantity', 0) > 0 and self.items[item].get('price', 0) > 0 for item in self.items):
        print("Pemesanan sudah benar")
    else:
        print("Terdapat kesalahan input data")
    print(tabulate([(name, details['quantity'], details['price']) for name, details in self.items.items()], headers=['Nama Item', 'Jumlah Item', 'Harga Item'], tablefmt='pretty'))
```

Metode ini memeriksa pesanan dengan memvalidasi kuantitas dan harga setiap item dalam transaksi. Jika semuanya benar, ia akan mencetak pesan konfirmasi; jika tidak, ia akan mencetak pesan kesalahan. Selain itu, ia juga mencetak detail transaksi dalam format tabel yang rapi.

### total_price(self) - Requirement

```python
def total_price(self):
    total = sum(details['quantity'] * details['price'] for details in self.items.values())
    if total > 500000:
        discount = 0.10
    elif total > 300000:
        discount = 0.08
    elif total > 200000:
        discount = 0.05
    else:
        discount = 0.0
    total_with_discount = total * (1 - discount)
    print(f"Total belanja: Rp. {total_with_discount:.2f}")
```

Metode ini menghitung total harga pesanan dengan menerapkan diskon berdasarkan total belanja. Diskon yang berlaku adalah: 10% untuk belanja di atas Rp 500.000, 8% untuk belanja di atas Rp 300.000, dan 5% untuk belanja di atas Rp 200.000.

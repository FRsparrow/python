n = 265188593383733426784462550243645925460788960236441455129027741961481208513810116205185314236205378557440303027652989389917619930442313605334365119212850935843556618956853065494720537323305574643047289853603211741043421558014754593640046092411651142662662831234030025970673305313107682699256884346103344089672890006693126771720096259672967891465169072027014082870822914378019193118562733655858746359435877441320883190038672322395036150645197730955760924775616601864266767227806056842945101626070575567064338708803715328731019663959483794699099051679252278719504607561291373461765034841530287485481692023822206025364473227160729219093444433734477645836618125649507813484572073961338071667894005103281160685528554906800017983270639654725215240426739822475072638187051654183
m = pow(2,65537,n)
c = 53614073375901982939609424045509928030196930357378451540205129689077361497100322799609125263530767514666835763363614116579781164627003950759930551271363249070035362130206818279054836734873425719671251061990618013654623439113627831131276772213763402119598953243284788442139026445702302087117066612897609876902146754862886491758957572578830773399702029131911508577735005657834449332686165610777653935047515042872017712330634341811543757221442387754673609123927718255324291173976881400241970207063982567956097849206879597543996638772842481003216038812688447207625547594346839374547365411950767523067444620972182166882678541864133920760678406346106543145047214600100570677613586881817999202370771026617272884838510926483624726778958939589861718419448514032571995789005220471
x = m * c % n
print(x>>1)

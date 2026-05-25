
![](_temp_c42f7c50_convert__images/_temp_c42f7c50_convert_.pdf-0001-00.png)


## _Article_ 

## **Principal Component Analysis of Biomass-Derived Carbon Aerogels: Unveiling Key Performance Factors for Supercapacitor Applications** 

**Khaled Younes[1,] * , Semaan Amine[1] , Christina El Sawda[1] , Samer El-Zahab[1] , Jack Arayro[1] , Rabih Mezher[1] , Jalal Halwani[2] , Baghdad Ouddane[3] and Eddie Gazo-Hanna[1]** 

- 1 College of Engineering and Technology, American University of the Middle East, Egaila 54200, Kuwait; semaan.amine@aum.edu.kw (S.A.); christina.el-sawda@aum.edu.kw (C.E.S.); samer.el-zahab@aum.edu.kw (S.E.-Z.); jack.arayro@aum.edu.kw (J.A.); rabih.mezher@aum.edu.kw (R.M.); eddie-hanna@aum.edu.kw (E.G.-H.) 

- 2 Water and Environment Sciences Laboratory, Lebanese University, Tripoli P.O. Box 6573/14, Lebanon; jhalwani@ul.edu.lb 

- 3 Laboratoire de Spectroscopie pour les Interactions, la Réactivité et l’Environnement, University of Lille, UMR CNRS 8516 LASIRE, 59000 Lille, France; baghdad.ouddane@univ-lille.fr 

- Correspondence: khaled.younes@aum.edu.kw 

## Academic Editors: Antonio D’Andrea and Wael Al-Kouz 

Received: 8 April 2025 Revised: 4 May 2025 Accepted: 14 May 2025 Published: 15 May 2025 

**Citation:** Younes, K.; Amine, S.; El Sawda, C.; El-Zahab, S.; Arayro, J.; Mezher, R.; Halwani, J.; Ouddane, B.; Gazo-Hanna, E. Principal Component Analysis of Biomass-Derived Carbon Aerogels: Unveiling Key Performance Factors for Supercapacitor Applications. _Sustainability_ **2025** , _17_ , 4530. https://doi.org/10.3390/ su17104530 

**Copyright:** © 2025 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/ licenses/by/4.0/). 

**Abstract:** The demand for sustainable energy storage solutions has led to increased interest in biomass-derived carbon aerogels as electrode materials for supercapacitors. These materials offer a high surface area, tunable porosity, and excellent electrochemical properties while utilizing renewable and waste biomass sources. This study evaluates the electrochemical performance of various biomass-based carbon aerogels, including those derived from cellulose, lignin, chitosan, and biomass waste, to identify key factors influencing supercapacitor efficiency. Principal Component Analysis (PCA) is employed to systematically analyze the relationships between structural and electrochemical properties, such as the specific surface area, specific capacitance, capacity retention, rate capability, energy density, and power density. The PCA results indicate that the first two principal components (PC1 and PC2) explain 58.20% of the total variance, with capacity retention (26.22%), energy density (19.55%), and specific capacitance (18.48%) identified as the most critical quantitative factors influencing supercapacitor performance. Chitosan-derived carbon aerogels exhibit superior capacitance and energy density, with a specific capacitance reaching up to 1074 F/g and energy density of 40.18 Wh/kg, whereas lignin-based aerogels demonstrate a high structural stability and capacity retention (up to 97.4%). Biomass wastederived aerogels, despite their lower performance (176–298.6 F/g capacitance, 81.6–91.7% retention), provide cost-effective and environmentally sustainable alternatives. This quantitative analysis offers valuable insights into the rational design of high-performance, biomass-based aerogels, contributing significantly to the development of sustainable energy storage technologies. 

**Keywords:** biomass-derived aerogels; supercapacitor; electrochemical performance; sustainable energy storage 

## **1. Introduction** 

The transition towards sustainable energy storage solutions is a crucial step in achieving the United Nations Sustainable Development Goals (SDGs), particularly SDG 7 (Affordable and Clean Energy), SDG 9 (Industry, Innovation, and Infrastructure), and SDG 12 

_Sustainability_ **2025** , _17_ , 4530 

https://doi.org/10.3390/su17104530 

_Sustainability_ **2025** , _17_ , 4530 

2 of 13 

(Responsible Consumption and Production). As the global demand for energy continues to rise, the need for efficient, renewable energy storage systems becomes more urgent. Traditional energy storage technologies, such as lithium-ion batteries, are associated with several challenges, including the limited availability of raw materials, environmental concerns, and high production costs [1]. Supercapacitors have emerged as promising alternatives due to their high power density, rapid charge–discharge cycles, and extended lifespan [2]. However, conventional supercapacitor materials, primarily derived from fossil fuels, pose sustainability challenges. 

In this context, biomass-based carbon aerogels represent an environmentally friendly alternative that aligns with sustainable energy initiatives. These materials, derived from renewable biomass sources, offer high porosity, excellent electrical conductivity, and tunable structural properties, making them attractive candidates for energy storage applications [3]. Moreover, their production leverages waste biomass resources, contributing to circular economy models and reducing dependence on non-renewable precursors [4]. The development of biomass-derived carbon aerogels for supercapacitors not only advances clean energy technologies but also supports resource efficiency and sustainable manufacturing, in line with global carbon neutrality efforts [5]. 

Biomass-based carbon aerogels have gained significant attention as electrode materials for supercapacitors due to their unique physicochemical properties, including ultralow density, large surface area, high electrical conductivity, and hierarchical porosity [6]. These properties enable efficient charge storage and rapid ion diffusion, enhancing the overall electrochemical performance of supercapacitors [1]. Biomass-derived carbon aerogels are synthesized from various renewable precursors, such as cellulose, lignin, chitosan, and biomass waste, each offering distinct advantages in material engineering. 

Recent studies have demonstrated that chitosan-derived carbon aerogels exhibit superior electrochemical stability due to high nitrogen doping levels, which enhance electron conductivity and pseudocapacitive behavior [4]. Similarly, lignin-derived carbon aerogels offer a high specific capacitance and structural integrity, making them suitable for applications requiring long-term cycling stability [2]. Furthermore, composite aerogels incorporating graphene or metal oxides have been explored to improve capacitance and power density [3]. Despite these advancements, further research is needed to optimize synthesis processes, enhance porosity control, and improve cost-effectiveness to facilitate large-scale commercial adoption. 

Principal Component Analysis (PCA) is a widely used multivariate statistical tool that facilitates the interpretation of large and complex datasets by reducing dimensionality while preserving key information [2]. In materials science, PCA has been extensively applied to analyze structure–property relationships, providing insights into material performance based on experimental variables [3]. For supercapacitor research, PCA enables the quantitative comparison of electrode materials, identifying patterns and correlations among parameters such as specific capacitance, energy density, power density, rate capability, and capacity retention. Although several review articles have summarized biomass-derived carbon aerogels’ electrochemical properties [7–11], quantitative comparative assessments using multivariate statistical tools such as PCA remain scarce. PCA systematically identifies the correlations between electrochemical properties, revealing hidden relationships crucial for optimizing aerogel performance. This quantitative insight provides clearer guidance for selecting appropriate biomass-derived materials based on specific performance criteria, distinguishing our approach from existing reviews that primarily offer qualitative assessments. 

For biomass-based carbon aerogels, PCA is particularly valuable in deciphering the contributions of surface area, porosity, and electrochemical properties to overall mate- 

_Sustainability_ **2025** , _17_ , 4530 

3 of 13 

rial performance. For instance, studies have shown that hierarchical porosity plays a crucial role in optimizing charge storage and ion diffusion, which can be effectively correlated using PCA [6]. Additionally, PCA has been employed to compare different biomass precursors, helping researchers identify optimal feedstocks for high-performance supercapacitor electrodes [4]. Given the complexity of electrochemical data, the systematic application of PCA provides a data-driven framework for guiding material development and performance optimization. The specific issue this study addresses is the absence of a comprehensive quantitative assessment framework to systematically compare various biomass-derived carbon aerogels for supercapacitor applications. Previous research predominantly offered qualitative comparisons of these materials, limiting the precise identification of performance-critical attributes. In response, the current study employs PCA as a novel quantitative approach to objectively rank biomass-based aerogels based on detailed electrochemical performance metrics. Compared to earlier studies, the novelty of our approach lies in quantitatively identifying the principal factors affecting electrochemical performance and systematically classifying aerogels derived from cellulose, lignin, chitosan, and biomass waste based on these factors. This methodology provides explicit, data-driven insights into material selection and optimization strategies, facilitating targeted engineering for improved energy storage efficiency. 

The primary objective of this study is to evaluate the performance of biomass-based carbon aerogels as electrode materials for supercapacitors using Principal Component Analysis (PCA). By analyzing a diverse set of aerogels, this study aims to identify the key factors influencing electrochemical performance and establish a comparative framework for different biomass-derived materials. The significance of this study lies in its ability to correlate material properties with functional performance, providing insights into the most influential variables affecting charge storage, cycling stability, and power density. 

The application of PCA offers a systematic approach to ranking and classifying aerogels, facilitating the rational design of next generation energy storage materials. This research aligns with global efforts to develop sustainable and high-performance supercapacitor materials, contributing to the broader adoption of biomass-derived energy storage solutions. Ultimately, the findings will aid in optimizing synthesis strategies, improving energy storage efficiency, and expanding the practical applications of biomass-based aerogels in the supercapacitor industry. 

## **2. Materials and Methods** 

## _2.1. Data Collection and Pre-Treatment_ 

Data have been collected from the published study of Li et al. [1]. Table 1 presents electrochemical features of biomass-derived carbon aerogels used for Principal Component Analysis (PCA). The table includes specific surface area (SSA), specific capacitance (Csp), capacity retention (CR), rate capability (Rate_Cap), energy density (E), and power density (P_density) for various biomass sources, including cellulose, lignin, chitosan, and biomass waste. The data of each of the investigated variables have different weights. In order to remove any bias yielded by the difference in magnitude, a normalization technique similar to the one presented in [12] has been adopted, as follows: 


![](_temp_c42f7c50_convert__images/_temp_c42f7c50_convert_.pdf-0003-08.png)


where “ _Yst_ ” presents the standardized dataset values. 

_Sustainability_ **2025** , _17_ , 4530 

4 of 13 

**Table 1.** Electrochemical properties of biomass-derived carbon aerogels used for Principal Component Analysis (PCA). The table includes specific surface area, specific capacitance, capacity retention, rate capability, energy density, and power density for various biomass sources, including cellulose, lignin, chitosan, and biomass waste. These parameters have been taken from Li et al. [1]. 

|**Biomass**|**Biomass Material**|**Specifc Surface**<br>**Area (m2/g)**|**Specifc**<br>**Capacitance**<br>**(F/g)**|**Capacity**<br>**Retention (%)**|**Rate Capability**<br>**(F/g)**|**Energy Density**<br>**(Wh kg**_−_**1)**|**Power Density**<br>**(kW kg**_−_**1)**|**Ref.**|
|---|---|---|---|---|---|---|---|---|
||Cellulose nanofbers<br>C-Nano|672|220.0|97.3|-|19.58|9.93|[13]|
|Cellulose|Bacterial cellulose<br>C-Bact|391|224|97|168|2.5|0.125|[14]|
||Cotton cellulose<br>C-Cot|1634.67|329|93|215|10.3|0.13|[3]|
||Agaric<br>C-Aga|2200|340|91|308|25.5|2|[15]|
|Lignin|Alkali lignin<br>Lig-Alk<br>Masson pine Kraft pulp<br>Lig-Kraft|1681.6<br>3742|189<br>504.7|97.4<br>87.7|14<br>-|26.25<br>18.1|1.0<br>16|[16]<br>[17]|
||Chitosan<br>CS-1|2435.2|197|92.1|820|27.4|0.4|[5]|
|Chitosan|Chitosan<br>CS-2|412.3|1074|94.3|-|40.18|0.8|[6]|
||Chitosan<br>CS-3|2529|195|91|-|6.8|0.251|[4]|
|Biomass waste|Ganoderma lucidum residues<br>Bio-GL<br>Enteromorpha prolifera waste<br>Bio-EP|893.9<br>2200|176<br>298.6|81.6<br>91.7|-<br>190|6.11<br>16.18|5<br>2.5|[2]<br>[18]|



_Sustainability_ **2025** , _17_ , 4530 

5 of 13 

## _2.2. Principal Component Analysis (PCA)_ 

After normalization, PCA findings were compiled using XLSTAT 2024.03 software (Addinsoft, Paris, France), following an approach similar to that adopted by Murshid et al. [19]. In this study, the missing data were estimated using a built-in feature that replaces a missing value with the “Mode”, following the respective variables. 

The aim of this study is to apply Principal Component Analysis (PCA) to the dataset of biomass-derived carbon aerogels used for supercapacitor applications (Table 1). The PCA aims to identify hidden relationships between the structural and electrochemical properties. Uncovering these correlations provides a deeper understanding of the key factors influencing the electrochemical performance of different aerogels. The insights gained from this analysis can guide material optimization strategies, aiding in the selection of high-performance aerogels for energy storage applications. In this study, PCA has been applied to six key electrochemical factors across various biomass-based aerogels, distinguishing high-performing materials from lower-performing ones (Table 1). PCA, as a data-driven unsupervised machine learning technique, reduces dataset dimensionality while preserving essential information. The results facilitate a clearer visualization of material performance trends, revealing underlying correlations (both positive and negative) and assessing the representativity of the principal components (pcs) in explaining the variance within the dataset. The _j_ th pc matrix ( _Fi_ ) is expressed using a unit-weighting vector ( _uj_ ) and the original data matrix m with _m × n_ dimensions ( _m_ : number of variables, _n_ : number of aerogels), as follows [20–25]: 


![](_temp_c42f7c50_convert__images/_temp_c42f7c50_convert_.pdf-0005-05.png)


where _u_ is the loading coefficient and _M_ is the data vector of size _n_ . The variance matrix _M_ ( _Var_ ( _M_ )), is obtained by projecting _M_ to _U_ , and should be maximized, as follows: 


![](_temp_c42f7c50_convert__images/_temp_c42f7c50_convert_.pdf-0005-07.png)



![](_temp_c42f7c50_convert__images/_temp_c42f7c50_convert_.pdf-0005-08.png)


Since _n_[1] _[MM][T]_[is][the][same][as][the][covariance][matrix][of] _[M]_[(] _[cov]_[(] _[M]_[)),] _[Var]_[(] _[M]_[)][can][be] expressed, as follows: 


![](_temp_c42f7c50_convert__images/_temp_c42f7c50_convert_.pdf-0005-10.png)


The Lagrangian function can be defined by performing the Lagrange multiplier method, as follows: 


![](_temp_c42f7c50_convert__images/_temp_c42f7c50_convert_.pdf-0005-12.png)


For (7), “ _U[T] U−_ 1” is considered to be equal to zero, since the weighting vector is a unit vector. Hence, the maximum value of _Var_ ( _M_ ) can be calculated by equating the derivative of the Lagrangian function ( _L_ ), in respect to _U_ , as follows: 


![](_temp_c42f7c50_convert__images/_temp_c42f7c50_convert_.pdf-0005-14.png)



![](_temp_c42f7c50_convert__images/_temp_c42f7c50_convert_.pdf-0005-15.png)


where 

_δ_ : eigenvalue of _cov_ ( _M_ ). 

_U_ : eigenvector of _cov_ ( _M_ ). 

_Sustainability_ **2025** , _17_ , 4530 

6 of 13 

## **3. Results and Discussion** 

## _3.1. Overview of Electrochemical Performance of Biomass-Based Carbon Aerogels_ 

The electrochemical performance of biomass-derived carbon aerogels has been extensively analyzed, highlighting their potential for energy storage applications. The properties of these aerogels, including their specific surface area, capacitance, energy density, and power density, vary significantly depending on the biomass precursor and synthesis conditions. The results, summarized in Table 1, reveal distinct advantages for different biomass sources in supercapacitor applications. 

Cellulose-derived carbon aerogels exhibit remarkable electrochemical characteristics due to their high surface area and stable structure. Cellulose nanofibers (C-Nano) demonstrate a specific capacitance of 220 F/g, coupled with an excellent capacity retention of 97.3%, making them suitable for long-term supercapacitor applications [13]. Similarly, bacterial cellulose (C-Bact), with a capacitance of 224 F/g, maintains its structural integrity with 97% retention, supporting its viability as an electrode material [14]. Among cellulose-based materials, cotton cellulose (C-Cot) shows a significantly higher surface area (1634.67 m[2] /g) and capacitance (329 F/g), yet a slightly lower retention (93%) [3]. Agaric-derived carbon aerogel (C-Aga) outperforms other cellulose-based aerogels, achieving a specific surface area of 2200 m[2] /g and a capacitance of 340 F/g, indicating its potential for high-energy applications [18]. 

Lignin-derived carbon aerogels exhibit some of the highest surface areas and capacitances among biomass-based materials. Alkali lignin (Lig-Alk) achieves a capacitance of 189 F/g with 97.4% retention, while offering an energy density of 26.25 Wh/kg, making it a promising candidate for sustainable energy storage [2]. On the other hand, the Masson pine Kraft pulp-derived aerogel (Lig-Kraft) reaches an outstanding surface area of 3742 m[2] /g and an impressive capacitance of 504.7 F/g, though its retention slightly decreases to 87.7% [17]. This suggests that Kraft lignin-based aerogels, with further optimization, could serve as high-performance electrode materials. 

Chitosan-derived carbon aerogels have demonstrated exceptional energy densities and capacitances. CS-1 and CS-2 exhibit capacitance values of 197 F/g and 1074 F/g, respectively, with CS-2 showing one of the highest energy densities at 40.18 Wh/kg, making it a prime candidate for high-power applications [5]. The superior performance of CS-2 is attributed to its hierarchical porous structure, which enhances ion transport and charge storage [6]. Conversely, CS-3 has a lower capacitance (195 F/g) but maintains 91% retention, indicating good stability despite slightly reduced performance [4]. 

Biomass waste-derived aerogels represent a cost-effective and environmentally friendly alternative to conventional carbon materials. Ganoderma lucidum residue-based carbon aerogel (Bio-GL) achieves a moderate capacitance of 176 F/g, though its retention is relatively lower than the previously mentioned materials, at 81.6% [2]. In contrast, Enteromorpha prolifera waste-derived aerogel (Bio-EP) displays a higher capacitance of 298.6 F/g with an improved retention of 91.7%, making it a more viable option for supercapacitor applications [18]. These results indicate that biomass waste-derived aerogels can serve as sustainable and cost-efficient materials for energy storage. 

The findings suggest that different biomass sources offer unique advantages in energy storage applications. Lignin-based aerogels exhibit high surface areas and capacitances, cellulose-derived aerogels provide a balance between performance and durability, chitosan aerogels offer exceptional energy densities, and biomass waste-derived aerogels present a low-cost, sustainable alternative. These results reinforce the potential of biomass-derived carbon aerogels as viable candidates for next-generation energy storage devices. The superior electrochemical performance of chitosan-derived carbon aerogels, particularly in capacitance and energy density, primarily arises from their nitrogen-doped carbon structure 

_Sustainability_ **2025** , _17_ , 4530 

7 of 13 

and hierarchical porous network [5]. Nitrogen doping enhances electrical conductivity and promotes pseudocapacitive behavior by introducing additional active sites for ion adsorption and electron transfer [5,26]. Conversely, lignin-based aerogels exhibit outstanding ~~structural stability and long-term cycling performance due to their inherently aromatic-rich~~ carbon networks, which contribute to mechanical robustness and chemical inertness, thus sustaining electrode integrity throughout prolonged cycling [16,17]. 

## _3.2. Principal Component Analysis (PCA) Interpretation of Biomass-Based Carbon Aerogels as Electrode Materials for Supercapacitors_ 

The Principal Component Analysis (PCA) of biomass-based carbon aerogels as electrode materials for supercapacitors revealed, in Figure 1, that the first two principal components (PC1 and PC2) accounted for 58.20% of the total variance, with 31.26% attributed to PC1 and 26.94% to PC2. This indicates that these two components capture more than half of the variability in the dataset, making them the most significant dimensions in differentiating the aerogels’ electrochemical performance. PC1 primarily represents a composite metric of performance influenced by specific electrochemical properties such as capacity retention and energy density, which have strong positive loadings, whereas PC2 is more associated with specific capacitance and energy density, as indicated by their high contributions. The relatively moderate contribution from power density suggests that while it plays a role in supercapacitor efficiency, it is not as dominant in defining the variance structure. 

## **Axes variance (58.20 %)** 


![](_temp_c42f7c50_convert__images/_temp_c42f7c50_convert_.pdf-0007-06.png)


**----- Start of picture text -----**<br>
1<br>Lig-Kraft<br>CS-2<br>0.8<br>E<br>SSA CS-1<br>0.6 Rate_Cap<br>Csp<br>0.4<br>0.2 P_density C-Aga<br>0<br>Bio-GL C-Nano<br>-0.2 Bio-EP<br>CR<br>-0.4 CS-3 Lig-Alk<br>C-Cot<br>-0.6<br>-0.8<br>-1 C-Bact<br>-1 -0.5 0 0.5 1<br>Principal Component 1 (31.26 %)<br>Principal Component 2 (26.94 %)<br>**----- End of picture text -----**<br>


**Figure 1.** PCA bi-plot of PC1 and PC2 for biomass-derived carbon aerogels, illustrating the distribution of materials (grey bullets) based on key electrochemical properties (white squares). 

A closer examination of the percentage contributions of the variables to PC1 and PC2, in Figure 2, provides further insights into their influence. PC1 is largely driven by capacity retention (26.22%), energy density (19.55%), and specific capacitance (18.48%), emphasizing that these attributes are crucial in distinguishing the aerogels’ overall performance. Meanwhile, PC2 is dominated by energy density (31.42%) and specific capacitance (22.86%), followed by rate capability (16.86%), showing that this component captures variations related to energy storage efficiency and charge/discharge dynamics. The dual role of energy density, significantly contributing to both PC1 and PC2, underscores its importance in influencing multiple aspects of supercapacitor performance. Additionally, the strong presence 

_Sustainability_ **2025** , _17_ , 4530 

8 of 13 

~~of specifc capacitance and rate capability in PC2 suggests that this component identifes~~ aerogels with enhanced charge storage capacity and rapid charge/discharge efficiency. 

## **Contribution of variables to PCs** 


![](_temp_c42f7c50_convert__images/_temp_c42f7c50_convert_.pdf-0008-04.png)


**----- Start of picture text -----**<br>
35<br>30<br>25<br>20<br>PC1<br>15<br>PC2<br>10<br>5<br>0<br>SSA Csp CR Rate_Cap E P_density<br>**----- End of picture text -----**<br>


**Figure 2.** % contribution of the first PCs presented in Figure 1. The analysis reveals that specific capacitance, energy density, and capacity retention are the dominant factors influencing material performance, distinguishing high-performing aerogels such as chitosan- and lignin-derived variants from lower-performing biomass waste-based aerogels. 

Analyzing the individual loadings of biomass-based carbon aerogels, significant differences emerge among the materials studied. The CS-2 aerogel, derived from chitosan, dominates both PC1 and PC2, with values of 1.00 and 0.805, respectively, confirming its superior overall electrochemical performance. This aligns with previous findings that CS-2 exhibited the highest specific capacitance and energy density [5]. The Lig-Kraft lignin aerogel, in contrast, has a strong positive loading on PC2 (0.95) but a negative correlation _−_ with PC1 ( 0.65), suggesting that while it performs well in energy-related attributes, it may be less effective in terms of retention or stability [17]. On the other end of the spectrum, biomass waste-derived aerogels such as Bio-GL and Bio-EP exhibit negative contributions to both PC1 and PC2, reinforcing previous findings that these materials generally underperform in terms of energy and power density [2]. The bacterial cellulose-based aerogel _−_ (C-Bact) has the most extreme negative PC2 value ( 1.00), indicating significant divergence in charge storage efficiency or charge/discharge dynamics. Overall, chitosan-derived aerogels (CS-1 and CS-2) and Kraft lignin aerogels stand out as the most promising materials in terms of key supercapacitor metrics (specific capacitance and energy density), whereas biomass waste-derived aerogels show a lower efficiency in these metrics. Unlike previous literature that primarily focuses on qualitative comparisons [7–9], our PCA-driven approach quantifies the relative importance of different electrochemical properties, such as specific capacitance, energy density, and capacity retention. These statistical insights help to clarify performance differences between aerogels derived from various biomass precursors, providing a more structured basis for material selection and development. 

Examining the factor loadings of performance metrics, specific capacitance and energy density show strong positive correlations with both PC1 (0.589 and 0.606, respectively) and PC2 (0.608 and 0.713, respectively), indicating that these two properties are crucial in distinguishing high-performance aerogels. These results confirm previous analyses where CS-2 and Lig-Kraft, both exhibiting high values in these properties, ranked among the top performers [5,17]. Capacity retention is strongly correlated with PC1 (0.701) but negatively _−_ associated with PC2 ( 0.269), suggesting that aerogels with high capacity retention tend to influence the overall performance rather than charge/discharge efficiency. Rate capability is more relevant to PC2 (0.522), playing a larger role in distinguishing materials based on rapid charge/discharge performance. Interestingly, specific surface area (SSA) is negatively correlated with PC1 ( _−_ 0.639) but positively associated with PC2 (0.464), implying that 

_Sustainability_ **2025** , _17_ , 4530 

9 of 13 

aerogels with a high SSA do not necessarily exhibit a superior overall performance but may still contribute to efficiency parameters such as capacitance or rate capability [3]. _−_ Power density shows a negative PC1 loading ( 0.471) and a moderate PC2 loading (0.422), suggesting that while it is an important factor, it is not the primary driver of aerogel differentiation. This aligns with previous findings where high-power density values were not always linked to superior electrochemical properties [2]. 

Comparing these PCA findings with the initial dataset analysis confirms many of the original trends, particularly the high performance of chitosan-derived aerogels and Kraft lignin aerogels, while reinforcing the lower efficiency of biomass waste-based aerogels. The PCA results strongly suggest that capacity retention, energy density, and specific capacitance are the most critical performance metrics for selecting high-performance aerogels. However, some discrepancies emerge. Specific surface area was expected to be a strong determinant of performance but showed mixed contributions in the PCA, suggesting that a larger SSA does not always correlate with better electrochemical properties. This is particularly evident in aerogels such as C-Cot and C-Aga, which have high SSA values but do not rank among the top PCA performers [3]. Power density also played a less significant role than expected, suggesting it may not be the best standalone metric for evaluating aerogel performance [2]. These PCA insights underline a critical relationship, as structural properties such as specific surface area and porosity directly influence electrochemical attributes including specific capacitance, capacity retention, and energy density. While a high specific surface area often enhances capacitance and ion transport efficiency, our findings indicate that the hierarchical pore structure and heteroatom doping (e.g., nitrogen doping in chitosan-based aerogels) could significantly amplify these electrochemical characteristics. This clarification provides a deeper understanding of how precise structural tuning can optimize electrochemical performance, guiding more targeted strategies for aerogel design. 

In brief, the PCA confirms most of the trends observed in the dataset while providing deeper insight into the factors that define high-performance aerogels. Chitosan-based aerogels emerge as the top candidates for supercapacitor applications due to their high specific capacitance and energy density, while Kraft lignin aerogels show promise due to their strong energy-related attributes. The weaker performance of biomass waste-derived aerogels further supports their lower ranking in previous analyses. The analysis also highlights the unexpected findings regarding specific surface area and power density, which appear to have a more complex influence on performance than initially assumed. These results reinforce the importance of capacity retention, energy density, and specific capacitance as key performance indicators for optimizing biomass-derived carbon aerogels for supercapacitor applications. Therefore, based on the PCA outcomes, capacity retention, energy density, and specific capacitance emerge as the principal quantitative factors essential for guiding the rational design and optimization of biomass-derived carbon aerogels for supercapacitor electrode applications. 

For the sake of maximizing the effectiveness of PCA in evaluating biomass-derived carbon aerogels, the analysis should ideally include comprehensive electrochemical and structural datasets from diverse materials. PCA’s ability to handle large, multidimensional datasets allows researchers to objectively rank materials based on multiple performance indicators simultaneously. Additionally, PCA results can be optimized by incorporating supplementary datasets, such as synthesis conditions, biomass type, and heteroatom doping levels, enabling more precise predictions and tailored material selection. Ultimately, utilizing PCA as demonstrated in this study offers a structured method to streamline the selection process, significantly enhancing efficiency in developing advanced supercapacitor electrode materials from biomass resources. 

_Sustainability_ **2025** , _17_ , 4530 

10 of 13 

_3.3. Principal Component Analysis (PCA) Interpretation of PC3 and PC4 for Biomass-Based Carbon Aerogels as Electrode Materials for Supercapacitors_ 

The third and fourth principal components (PC3 and PC4) accounted for 29.94% of the total variance, with PC3 contributing by 17.70% and PC4 by 12.24% (Figure 3). While PC1 and PC2 primarily captured variations related to energy storage capacity and charge storage efficiency, PC3 and PC4 reveal additional trends related to power-related behavior, charge–discharge dynamics, and structural stability in biomass-derived carbon aerogels. 

## **Axes variance (29.94 %)** 


![](_temp_c42f7c50_convert__images/_temp_c42f7c50_convert_.pdf-0010-05.png)


**----- Start of picture text -----**<br>
1<br>0.8<br>Lig-Alk<br>0.6 CR<br>0.4 C-Nano SSA<br>Lig-Kraft<br>0.2 E CS-3 CS-1<br>0 Bio-EP C-Aga<br>C-Bact<br>-0.2 P_density C-Cot Rate_Cap<br>Csp<br>-0.4<br>CS-2<br>-0.6<br>-0.8<br>Bio-GL<br>-1<br>-1 -0.5 0 0.5 1<br>Principal Component 4 (12.24 %)<br>**----- End of picture text -----**<br>


Principal Component 3 (17.70 %) 

**Figure 3.** PCA bi-plot of PC3 and PC4 for biomass-derived carbon aerogels, illustrating the distribution of materials (grey bullets) based on key electrochemical properties (white squares). 

PC3 is highly dominated by rate capability (53.71%) and power density (36.24%), indicating that this component strongly differentiates aerogels based on their fast charge/discharge performance and high-power applications (Figure 4). This aligns with observations found by Xu et al. [2], who emphasized the fact that aerogels with optimized hierarchical porosity tend to exhibit a superior rate capability [2]. Meanwhile, PC4 is primarily characterized by capacity retention (52.84%) and specific surface area (26.03%), suggesting the capture of differences in structural stability and surface-driven charge storage rather than immediate power-handling capabilities (Figure 4). The strong presence of capacity retention in PC4, which was also significant in PC1, reinforces its importance in defining the overall aerogel performance, as discussed by Cui et al. [18] in their study on the role of hierarchical porosity in maintaining long-term stability [18]. 

The factor loadings for individual aerogels reveal that CS-1 exhibits the highest PC3 loading (1.00), confirming its strong performance in rate capability and power-intensive applications. This is consistent with findings realized by Dang et al. [3], who demonstrated that certain chitosan-based aerogels exhibit excellent high-power handling due to optimized nitrogen doping [3]. Conversely, CS-2, which previously dominated PC1 and PC2, now _− −_ shows negative loadings for both PC3 ( 0.1652) and PC4 ( 0.5465), reinforcing that while it is optimized for energy storage, CS-2 is not well suited for rapid charge–discharge cycles. Similarly, Lig-Alk demonstrates a strong positive PC4 loading (0.5819), suggesting that this aerogel benefits from high retention and structural integrity, findings that echo those obtained by Li et al. [1] on the structural stability of lignin-derived aerogels for energy storage applications. 

_Sustainability_ **2025** , _17_ , 4530 

11 of 13 

## **Contribution of variables to PCs** 


![](_temp_c42f7c50_convert__images/_temp_c42f7c50_convert_.pdf-0011-03.png)


**----- Start of picture text -----**<br>
60<br>50<br>40<br>30 PC3<br>20 PC4<br>10<br>0<br>SSA Csp CR Rate_Cap E P_density<br>**----- End of picture text -----**<br>


**Figure 4.** % contribution of the first PCs presented in Figure 3. The analysis reveals that rate capability, power density, and capacity retention are the dominant factors influencing material performance, distinguishing aerogels in terms of charge–discharge efficiency and structural stability. 

For biomass waste-derived aerogels (Bio-GL and Bio-EP), their negative contributions to both PC3 and PC4 confirm their overall underperformance, particularly in stability and _−_ power-related metrics. Bio-GL exhibits the lowest PC4 loading ( 1.00), reinforcing the idea that it suffers from poor capacity retention and structural limitations, while Bio-EP remains neutral in both components, further suggesting an overall lack of competitive electrochemical properties (Figure 3). This trend was also observed in previous studies on low-rate performance of waste-derived carbon aerogels [6]. 

The factor loadings of performance metrics further emphasize the distinction between PC3 and PC4. PC3 is primarily dictated by rate capability (0.7552), while power density _−_ contributes negatively ( 0.6204), reinforcing that high charge–discharge efficiency does not always correlate with sustained high-power output. Meanwhile, PC4 is strongly influenced by capacity retention (0.6229) and SSA (0.4372), suggesting that aerogels with higher retention tend to have larger surface areas, emphasizing their structural stability and material durability (Figure 3). 

In summary, PC3 identifies aerogels optimized for high power and charge–discharge efficiency, whereas PC4 focuses on stability and surface-driven charge storage properties. CS-1 emerges as the strongest performer in PC3, highlighting its advantage in rapid charge–discharge cycles, whereas Lig-Alk dominates PC4, emphasizing its superior capacity retention and structural resilience. These findings further confirm the specialized nature of biomass-derived carbon aerogels, where some materials excel in energy storage while others perform better under high power conditions or long-term cycling. 

## **4. Conclusions** 

This study provides a comprehensive Principal Component Analysis (PCA) of biomassbased carbon aerogels as electrode materials for supercapacitors, identifying key performance attributes and material-specific advantages. The findings reveal that PC1 and PC2, which account for 58.20% of the total variance, primarily distinguish aerogels based on energy storage efficiency, specific capacitance, and capacity retention. The superior performance of chitosan-derived aerogels (CS-2) and Kraft lignin aerogels (Lig-Kraft) in these components highlights their suitability for applications requiring a high energy density and long-term stability. Conversely, the biomass waste-derived aerogels (BioGL and Bio-EP) exhibited lower rankings across PC1 and PC2, reaffirming their limited electrochemical viability. 

In contrast, PC3 and PC4, which, together, contribute 29.94% of the total variance, highlight the role of rate capability, power density, and structural stability in aerogel differentiation. CS-1 emerged as the strongest performer in PC3, confirming its high-rate 

_Sustainability_ **2025** , _17_ , 4530 

12 of 13 

performance and fast charge–discharge capability, while Lig-Alk dominated PC4, indicating its enhanced structural resilience and its high-capacity retention. These insights confirm that aerogels optimized for energy storage (PC1-PC2) do not necessarily perform best in high-power applications (PC3), emphasizing the importance of tailoring material selection based on specific supercapacitor requirements. 

Overall, this study reinforces the critical role of hierarchical porosity, nitrogen doping, and carbon structure optimization in enhancing aerogel performance. The PCA-driven classification provides a strategic framework for selecting biomass-derived carbon aerogels suited for different supercapacitor applications, whether high-energy storage, rapid charge–discharge cycles, or long-term stability. Future research should focus on further optimizing synthesis techniques, integrating heteroatom doping strategies, and enhancing power density without compromising stability, ensuring the continued advancement of sustainable, high-performance supercapacitor materials. 

**Author Contributions:** Conceptualization, K.Y.; methodology, K.Y.; validation, K.Y., E.G.-H. and S.A.; formal analysis, K.Y., E.G.-H. and S.A.; investigation, K.Y., R.M., J.A., C.E.S., S.E.-Z., S.A. and E.G.-H.; data curation, K.Y.; writing—original draft preparation, K.Y., R.M., J.A., C.E.S., S.E.-Z., S.A. and E.G.-H.; writing—review and editing, K.Y., E.G.-H., J.H., B.O. and S.A.; visualization, K.Y., R.M., J.A., C.E.S., S.E.-Z., S.A. and E.G.-H.; supervision, K.Y., B.O. and J.H.; project administration, K.Y. and E.G.-H. All authors have read and agreed to the published version of the manuscript. 

**Funding:** This research received no external funding. 

**Institutional Review Board Statement:** Not applicable. 

**Informed Consent Statement:** Not applicable. 

**Data Availability Statement:** The data presented and treated in this study are available from Sustainable Biomass-Derived Carbon Aerogels for Energy Storage Applications. [DOI: https://doi. org/10.1016/j.cej.2024.156693]. 

**Conflicts of Interest:** The authors declare no conflicts of interest. 

## **References** 

1. Li, M.; Pang, B.; Dai, S.; Cui, Y.; Wu, Y.; Li, H.; Luo, B. Sustainable Biomass-Derived Carbon Aerogels for Energy Storage Applications. _Chem. Eng. J._ **2024** , _499_ , 156693. [CrossRef] 

2. Xu, M.; Wang, A.; Xiang, Y.; Niu, J. Biomass-Based Porous Carbon/Graphene Self-Assembled Composite Aerogels for High-Rate Performance Supercapacitor. _J. Clean. Prod._ **2021** , _315_ , 128110. [CrossRef] 

3. Dang, C.; Huang, Z.; Chen, Y.; Zhou, S.; Feng, X.; Chen, G.; Dai, F.; Qi, H. Direct Dissolution of Cellulose in NaOH/Urea/α-Lipoic Acid Aqueous Solution to Fabricate All Biomass-Based Nitrogen, Sulfur Dual-Doped Hierarchical Porous Carbon Aerogels for Supercapacitors. _ACS Appl. Mater. Interfaces_ **2020** , _12_ , 21528–21538. [CrossRef] [PubMed] 

4. Gao, Y.; Zheng, S.; Fu, H.; Ma, J.; Xu, X.; Guan, L.; Wu, H.; Wu, Z.-S. Three-Dimensional Nitrogen Doped Hierarchically Porous Carbon Aerogels with Ultrahigh Specific Surface Area for High-Performance Supercapacitors and Flexible Micro-Supercapacitors. _Carbon_ **2020** , _168_ , 701–709. [CrossRef] 

5. Hao, P.; Zhao, Z.; Leng, Y.; Tian, J.; Sang, Y.; Boughton, R.; Wong, C.P.; Liu, H.; Yang, B. Graphene-Based Nitrogen Self-Doped Hierarchical Porous Carbon Aerogels Derived from Chitosan for High Performance Supercapacitors. _Nano Energy_ **2015** , _15_ , 9–23. [CrossRef] 

6. Ma, L.; Sun, G.; Ran, J.; Lv, S.; Shen, X.; Tong, H. One-Pot Template-Free Strategy toward 3D Hierarchical Porous Nitrogen-Doped Carbon Framework in Situ Armored Homogeneous NiO Nanoparticles for High-Performance Asymmetric Supercapacitors. _ACS Appl. Mater. Interfaces_ **2018** , _10_ , 22278–22290. [CrossRef] [PubMed] 

7. Zhu, X.; Zeng, Y.; Zhao, X.; Liu, D.; Lei, W.; Lu, S. Biomass-Derived Carbon and Their Composites for Supercapacitor Applications: Sources, Functions, and Mechanisms. _EcoEnergy_ **2025** , _4_ , e70000. [CrossRef] 

8. Gao, X.; Xing, Z.; Li, Z.; Dong, X.; Ju, Z.; Guo, C. A Review on Recent Advances in Carbon Aerogels: Their Preparation and Use in Alkali-Metal Ion Batteries. _New Carbon Mater._ **2020** , _35_ , 486–507. [CrossRef] 

9. Lu, W.; Si, Y.; Zhao, C.; Chen, T.; Li, C.; Zhang, C.; Wang, K. Biomass-Derived Carbon Applications in the Field of Supercapacitors: Progress and Prospects. _Chem. Eng. J._ **2024** , _495_ , 153311. [CrossRef] 

_Sustainability_ **2025** , _17_ , 4530 

13 of 13 

10. Joliffe, I.; Morgan, B. Principal Component Analysis and Exploratory Factor Analysis. _Stat. Methods Med. Res._ **1992** , _1_ , 69–95. [CrossRef] 

11. Younes, K.; Kharboutly, Y.; Antar, M.; Chaouk, H.; Obeid, E.; Mouhtady, O.; Abu-samha, M.; Halwani, J.; Murshid, N. Application of Unsupervised Learning for the Evaluation of Aerogels’ Efficiency towards Dye Removal—A Principal Component Analysis (PCA) Approach. _Gels_ **2023** , _9_ , 327. [CrossRef] [PubMed] 

12. Chaouk, H.; Obeid, E.; Halwani, J.; Arayro, J.; Mezher, R.; Mouhtady, O.; Gazo Hanna, E.; Amine, S.; Younes, K. Machine Learning Techniques to Analyze the Influence of Silica on the Physio-Chemical Properties of Aerogels. _Gels_ **2024** , _10_ , 554. [CrossRef] [PubMed] 

13. Long, S.; Feng, Y.; He, F.; Zhao, J.; Bai, T.; Lin, H.; Cai, W.; Mao, C.; Chen, Y.; Huigan, G.; et al. Biomass-Derived, Multifunctional and Wave-Layered Carbon Aerogels toward Wearable Pressure Sensors, Supercapacitors and Triboelectric Nanogenerators. _Nano Energy_ **2021** , _85_ , 105973. [CrossRef] 

14. Chen, H.; Liu, T.; Mou, J.; Zhang, W.; Jiang, Z.; Liu, J.; Huang, J.; Liu, M. Free-Standing N-Self-Doped Carbon Nanofiber Aerogels for High-Performance All-Solid-State Supercapacitors. _Nano Energy_ **2019** , _63_ , 103836. [CrossRef] 

15. Zhang, H.; Zhang, Z.; Luo, J.-D.; Qi, X.-T.; Yu, J.; Cai, J.-X.; Wei, J.; Yang, Z.-Y. A Chemical Blowing Strategy to Fabricate BiomassDerived Carbon-Aerogels with Graphene-Like Nanosheet Structures for High-Performance Supercapacitors. _ChemSusChem_ **2019** , _12_ , 2462–2470. [CrossRef] 

16. Zhang, Y.; Zhao, C.; Ong, W.K.; Lu, X. Ultrafast-Freezing-Assisted Mild Preparation of Biomass-Derived, Hierarchically Porous, Activated Carbon Aerogels for High-Performance Supercapacitors. _ACS Sustain. Chem. Eng._ **2019** , _7_ , 403–411. [CrossRef] 

17. Wang, T.; Liu, Z.; Li, P.; Wei, H.; Wei, K.; Chen, X. Lignin-Derived Carbon Aerogels with High Surface Area for Supercapacitor Applications. _Chem. Eng. J._ **2023** , _466_ , 143118. [CrossRef] 

18. Cui, J.; Xi, Y.; Chen, S.; Li, D.; She, X.; Sun, J.; Han, W.; Yang, D.; Guo, S. Prolifera-Green-Tide as Sustainable Source for Carbonaceous Aerogels with Hierarchical Pore to Achieve Multiple Energy Storage. _Adv. Funct. Mater._ **2016** , _26_ , 8487–8495. [CrossRef] 

19. Murshid, N.; Mouhtady, O.; Abu-Samha, M.; Obeid, E.; Kharboutly, Y.; Chaouk, H.; Halwani, J.; Younes, K. Metal Oxide Hydrogel Composites for Remediation of Dye-Contaminated Wastewater: Principal Component Analysis. _Gels_ **2022** , _8_ , 702. [CrossRef] 

20. Younes, K.; Laduranty, J.; Descostes, M.; Grasset, L. Molecular Biomarkers Study of an Ombrotrophic Peatland Impacted by an Anthropogenic Clay Deposit. _Org. Geochem._ **2017** , _105_ , 20–32. [CrossRef] 

21. Younes, K.; Grasset, L. Analysis of Molecular Proxies of a Peat Core by Thermally Assisted Hydrolysis and Methylation-Gas Chromatography Combined with Multivariate Analysis. _J. Anal. Appl. Pyrolysis_ **2017** , _124_ , 726–732. [CrossRef] 

22. Korichi, W.; Ibrahimi, M.; Loqman, S.; Ouhdouch, Y.; Younes, K.; Lemée, L. Assessment of Actinobacteria Use in the Elimination of Multidrug-Resistant Bacteria of Ibn Tofail Hospital Wastewater (Marrakesh, Morocco): A Chemometric Data Analysis Approach. _Environ. Sci. Pollut. Res._ **2021** , _28_ , 26840–26848. [CrossRef] [PubMed] 

23. Younes, K.; Grasset, L. The Application of DFRC Method for the Analysis of Carbohydrates in a Peat Bog: Validation and Comparison with Conventional Chemical and Thermochemical Degradation Techniques. _Chem. Geol._ **2020** , _545_ , 119644. [CrossRef] 

24. Obeid, E.; Younes, K. Uncovering Key Factors in Graphene Aerogel-Based Electrocatalysts for Sustainable Hydrogen Production: An Unsupervised Machine Learning Approach. _Gels_ **2024** , _10_ , 57. [CrossRef] 

25. Gazo Hanna, E.; Younes, K.; Amine, S.; Roufayel, R. Exploring Gel-Point Identification in Epoxy Resin Using Rheology and Unsupervised Learning. _Gels_ **2023** , _9_ , 828. [CrossRef] 

26. Zhao, K.; Sun, X.; Wang, Z.; Huang, C.; Li, D.; Liu, J. Sheet-like NiCo-Layered Double Hydroxide Anchored on N Self-Doped Hierarchical Porous Carbon Aerogel from Chitosan for High-Performance Supercapacitors. _J. Alloys Compd._ **2022** , _921_ , 166036. [CrossRef] 

**Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content. 


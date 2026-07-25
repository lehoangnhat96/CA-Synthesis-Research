International Journal of Electrochemical Science 20 (2025) 101209 


![](_temp_30dedc3c_convert__images/_temp_30dedc3c_convert_.pdf-0001-01.png)


Contents lists available at ScienceDirect 

## International Journal of Electrochemical Science 

journal homepage: www.sciencedirect.com/journal/international-journal-of-electrochemical-science 


![](_temp_30dedc3c_convert__images/_temp_30dedc3c_convert_.pdf-0001-05.png)


## Recent progress of electrochemical sensors for accurate detection of heavy metal ions in water: A comprehensive review 


![](_temp_30dedc3c_convert__images/_temp_30dedc3c_convert_.pdf-0001-07.png)


## Jing Liu[a][,][b] , Yuan Yin[a][,][b][,][*] , Gang Liu[c][,][d] 

a _School of Electronic and Electrical Engineering, Wuhan Textile University, Wuhan 430200, China_ 

b _Hubei Province Engineering Research Centre for Intelligent Micro-nano Medical Equipment and Key Technologies, Wuhan 430200, China_ 

c _Key Lab of Smart Agriculture System Integration Research, Ministry of Education of China, China Agricultural University, Beijing 100083, China_ 

d _Key Lab of Agriculture Information Acquisition Technology, Ministry of Agriculture and Rural Affairs of China, China Agricultural University, Beijing 100083, China_ 

A R T I C L E I N F O A B S T R A C T _Keywords:_ Water pollution represents a critical global environmental challenge, with heavy metal ions constituting a major Heavy metal ions class of contaminants. These toxic ions enter the human body through multiple pathways, including the conPollution sumption of contaminated drinking water, dermal contact, and bioaccumulation in the food chain. Once introElectrochemistry duced, they pose severe health risks due to their high toxicity, strong bioaccumulation potential, and slow Electrochemical sensors excretion rate. Such characteristics enable them to accumulate over time, creating long-term threats to both Machine learning algorithms ecosystems and public health. Addressing these risks requires the development of highly sensitive, accurate, and reliable detection methods to monitor and identify heavy metal pollutants effectively, thereby ensuring environmental monitoring and public health protection. The growing prominence of electrochemical sensing devices in the identification and quantification of toxic metal ions is attributed to their low cost, high selectivity, exceptional sensitivity, and ability to achieve very low detection limits. This review provides a comprehensive overview of recent developments in electrochemical sensing platforms for monitoring heavy metals in aqueous environments and identifies emerging directions for future research. The review is structured to first examine electrode fabrication strategies, detailing the properties of electrodes and the characteristics of electrodes produced through various methods. Next, it reviews research progress concerning the modification of electrodes, emphasizing a variety of modifying materials, including inorganic compounds, organic frameworks, and biomaterials. Subsequently, progress in the supporting analytical frameworks is discussed, including signal recognition, data processing, and predictive modeling algorithms that enable intelligent analysis. Finally, current trends in electrochemical sensing are summarized, and perspectives are offered for the development of novel electrochemical sensor technologies for reliable and precise detection of heavy metal ions. 

## **1. Introduction** 

Environmental pollution, encompassing atmospheric, soil, and water contamination, has emerged as a critical global concern. Among these, water pollution presents particularly urgent threats due to its direct and detrimental effects on human health, biodiversity, and ecosystem stability. The degradation of freshwater resources underscores this crisis; the World Health Organization (WHO) estimates that pollution renders nearly 20 % of global freshwater resources unusable, thereby severely constraining sustainable development and economic growth [1,2]. Among water pollutants, heavy metals are particularly hazardous because of their environmental persistence, bioaccumulation potential, 

and high toxicity. The economic repercussions are profound, with annual damages from aquatic heavy metal pollution already exceeding trillions of dollars, with projections indicating even greater costs in the future [3]. 

Once introduced into aquatic environments, toxic metal ions, such as lead (Pb), cadmium (Cd), mercury (Hg), and arsenic (As), enter the human body primarily through contaminated drinking water and bioaccumulation in the food chain. These toxicants cause irreversible damage to critical physiological systems, including the nervous, immune, and reproductive systems. This damage results in severe health disorders, such as cognitive impairment, elevated cancer incidence, and congenital abnormalities [4,5]. Chronic exposure to heavy 

- Corresponding author at: School of Electronic and Electrical Engineering, Wuhan Textile University, Wuhan 430200, China. _E-mail address:_ 2023009@wtu.edu.cn (Y. Yin). 

https://doi.org/10.1016/j.ijoes.2025.101209 

Received 1 September 2025; Received in revised form 13 October 2025; Accepted 13 October 2025 Available online 14 October 2025 

1452-3981/© 2025 The Author(s). Published by Elsevier B.V. on behalf of ESG. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-nc-nd/4.0/ ). 

> _J. Liu et al.                                                                                                                                                                                                                                       International Journal of Electrochemical Science 20 (2025) 101209_ 

metal-contaminated water significantly elevates the risk of multiple pathologies. For example, long-term ingestion of Cd-contaminated water induces neurotoxicity, causing particularly devastating effects on fetal and child development [6]. Cadmium accumulation also impairs renal function, contributing to progressive kidney damage that may culminate in chronic kidney disease and potential renal failure [7]. Similarly, chronic Hg exposure through contaminated water compromises immune function and reproductive health [8]. Prolonged ingestion of As-contaminated water has been strongly associated with increased risk of several cancers, particularly those affecting the skin, lungs, and bladder [9]. Given these severe health threats, the development of precise and efficient methods for detecting heavy metal concentrations in aquatic systems has become imperative. Such technological advancements are crucial for safeguarding public water supplies, preserving ecosystem balance, and promoting environmental sustainability [10]. 

Commonly used analytical methods, including atomic absorption spectroscopy (AAS) [11], inductively coupled plasma mass spectrometry (ICP-MS) [12], and laser-induced breakdown spectroscopy (LIBS) [13], are widely recognized for their high precision and sensitivity in detecting heavy metals in aqueous samples [14]. Despite their analytical accuracy, these conventional methods face notable limitations, including high operational costs, complex instrumentation, and time-intensive procedures. These limitations restrict their practicality for the rapid, routine, and cost-effective detection of heavy metal ions in water [15]. 

Unlike traditional detection methods, sensing technologies are increasingly regarded as promising alternatives, offering several distinct advantages. These include: (i) cost-effectiveness, as these systems require significantly lower capital and operational expenditures than traditional spectrometric methods; (ii) operational simplicity, with streamlined procedures that minimize technical expertise requirements, making the technology more accessible for routine use; (iii) high portability, enabled by compact designs that facilitate on-site deployment and field analysis; (iv) rapid response capability, allowing for accurate results within short timeframes to real-time environmental monitoring and timely decision-making for pollution control [16–18]. 

Furthermore, the operating principle of electrochemical sensors is based on redox reactions that occur at the interface between the electrode surfaces and heavy metal ions. The specific oxidation states of metal ions are identified by monitoring variations in electrical potential, while their concentrations are quantified through the corresponding current responses. This mechanism enables rapid and highly sensitive detection, making it particularly suitable for identifying trace levels of heavy metals in aqueous environments. However, several challenges remain, particularly in enhancing the sensitivity, selectivity, and overall measurement accuracy of electrochemical devices used for heavy metal detection [19–21]. 

This review assesses recent advancements in electrochemical techniques for detecting heavy metals in aqueous samples, providing an indepth analysis of relevant research from the past five years (2021–2025） to identify critical future research directions. Although several reviews on electrochemical sensors for heavy metal ion detection have been published, most focus primarily on a single category of sensing materials, such as inorganic, organic, or biomaterials, for sensor fabrication. In contrast, this review provides a systematic and comparative analysis of sensors fabricated from all these material classes, offering a unified perspective on their respective advantages and limitations. A further novel contribution is the detailed examination of machine learning (ML) integration within this field, highlighting its role in overcoming the persistent challenges of complex electrochemical data analysis. This integration signifies a paradigm shift from mere "data acquisition" to "intelligent analysis," significantly enhancing detection accuracy and reliability by resolving issues such as signal overlap and baseline drift. The move toward ML-driven, self-adaptive, highprecision intelligent sensing systems is highlighted as a pivotal future 

trend. The review is structured to first present a systematic evaluation of electrode performance characteristics across various fabrication methodologies. It subsequently discusses innovative electrode modification strategies using advanced materials, including nanostructured inorganic compounds (e.g., metallic, metal oxide, and carbon-based nanomaterials), functional organic polymers (e.g., small molecules and polymers), and bio-inspired substrates (e.g., DNA and enzymes). Recent computational enhancements are then analyzed, with a focus on algorithm-based advancements in signal recognition, processing, and predictive modeling. The review concludes by highlighting emerging trends to inform the future design of high-performance sensors for aquatic heavy metal monitoring. 

## **2. Process for heavy metal ion detection using stripping voltammetry** 

Stripping voltammetry is widely recognized as a highly sensitive electrochemical technique for trace-level heavy metal ion detection. The methodology comprises two principal stages: (1) a preconcentration step, in which target ions are electrochemically reduced and deposited onto the working electrode surface at a controlled potential, and (2) a stripping step, where a positive potential sweep is used to reoxidize the deposited metals, stripping them back into the solution. The resulting current– potential profile enables qualitative identification through characteristic peak potentials and quantitative determination from peak current intensities [22,23]. In stripping voltammetry, detecting heavy metal ions involves two distinct electrochemical processes: the deposition phase, where the target metal ions undergo electrochemical reduction and accumulate on the sensor surface, and the stripping phase, where the deposited metals are reoxidized and released back into the solution [24]. During the anodic stripping phase, as the applied poten– tial sweeps positively (typically at 10 100 mV/s), the electrodeposited metals are oxidatively stripped as the applied potential exceeds their redox potentials. The Faradaic current increases as the potential approaches the characteristic half-wave potential (E₁/₂) for each metal, reaching a maximum current (iₚ) at E₁/₂. The current then decays as the surface concentration of the metal is depleted, until the oxidative stripping process is complete [25–27]. A schematic illustration of this process is provided in Fig. 1. 

In summary, stripping voltammetry provides a powerful approach for analyzing heavy metal ions, enabling both qualitative identifications through distinct voltammetric peak potentials and quantitative determination via corresponding peak current measurements. The performance of these electrochemical sensors is governed by three critical characteristics: (i) interference resistance, which is dictated by electrode fabrication methodologies; (ii) detection sensitivity, which is controlled by electrode modification strategies; and (iii) measurement accuracy, which can be significantly enhanced through machine learning integration [28–31]. Consequently, this review focuses on two pivotal areas: advanced electrode modification strategies and the integration of ML algorithms for data analysis. This section provides a comprehensive overview of current advancements and emerging approaches for optimizing sensor performance in heavy metal detection. 

The electrode functions as the core component of an electrochemical sensing platform, with its interfacial properties directly dictating critical analytical performance metrics, such as sensitivity, selectivity, stability, and reproducibility. The following section introduces several common electrode fabrication methods and the characteristics of the resulting electrodes, with a summary provided in Table 1. 

## **3. Electrode modification materials for enhanced heavy metal detection** 

## _3.1. Inorganic modification materials_ 

Inorganic nanomaterials are indispensable in electrochemical sensor 

2 

_International Journal of Electrochemical Science 20 (2025) 101209_ 


![](_temp_30dedc3c_convert__images/_temp_30dedc3c_convert_.pdf-0003-02.png)


**Fig. 1.** Process for Heavy Metal Ion Detection Using Stripping Voltammetry. 

design due to their distinct advantages, such as excellent thermal stability, high specific surface area, and superior catalytic efficiency [32]. These properties enhance sensor sensitivity and selectivity by providing efficient electron-transfer pathways and abundant active sites for signal amplification [33,34]. This section critically examines representative inorganic modifiers, including metallic nanoparticles, metal oxides, and carbon-based nanomaterials. Their corresponding sensing mechanisms are detailed in Table 2. 

## _3.1.1. Metallic nanoparticles_ 

Metallic nanomaterials possess distinct physicochemical properties, such as high surface-to-volume ratios, uniform particle size distribution, and excellent electrical, optical, and catalytic performance, that make them highly suitable for sensor applications [35]. These attributes substantially improve electrochemical sensor performance by enhancing detection sensitivity, broadening the linear detection range, and improving selectivity for heavy metal ions [36]. Among these materials, noble metal nanoparticles, particularly gold (Au), platinum (Pt), and silver (Ag), have emerged as highly effective electrode modifiers in aqueous heavy metal detection systems because of their optimal combination of these functional properties [37]. 

Gold nanoparticles (AuNPs) are highly stable and serve as excellent modifiers for electrochemical sensors. They offer numerous advantages, including exceptional charge transport properties, thermal conduction properties, high chemical inertness, large specific area, and good biocompatibility. The AuNP surfaces can be readily functionalized with a wide range of organic and biological molecules, including graphene, polymers, DNA, and enzymes, enabling their integration into diverse sensing platforms [38,39]. In electrochemical sensor development, AuNPs are widely used due to their tunable electrical properties, which can be precisely controlled by adjusting experimental parameters such as particle dimensions and morphology [40]. However, the high cost of gold remains a limitation, and economic feasibility must be considered when utilizing AuNPs as electrode modification materials. Chen et al. [41] recently developed an innovative sensor based on a three-dimensional (3D) MXene-AuNPs hybrid, synthesized via _in situ_ chemical reduction to uniformly grow AuNPs on MXene nanosheets. To enhance ion selectivity, the AuNPs were functionalized with three distinct thiol (-SH) modifiers specifically tailored for the simultaneous detection of Pb²⁺, Cu²⁺, and Hg²⁺. When implemented on an ITO array electrode, this platform demonstrated exceptional sensitivity, achieving low detection limits (LODs) of 0.07 μg/L for Pb²⁺, 0.13 μg/L for Cu²⁺, and 0.21 μg/L for Hg²⁺, with a wide linear response range of 1–1300 μg/L for all three ions. In validation tests using real wastewater samples, the sensor’s results showed strong agreement with the benchmark ICP-MS method, with minimal relative errors (3.3 %). The low relative standard deviation (RSD) values (3.3 %) further confirmed its high precision 

and robustness against complex sample matrices. While these results are highly promising, further validation with a larger and more diverse set of real environmental samples, such as river water, soil leachate, and ’ biological fluids, is necessary to comprehensively establish the sensor resistance to matrix effects and its general applicability across different scenarios. In a complementary study, Kullavadee et al. [42] developed a sensor using an AuNP-functionalized screen-printed electrode for the simultaneous detection of Cd[2][ +] , Pb[2][+] , As[3][+] , and Hg[2][+] in tap water using differential pulse anodic stripping voltammetry (DPASV). The sensor demonstrated detection limits of 9.4 μg/L for Cd²⁺, 4.4 μg/L for Pb²⁺, 7.6 μg/L for As[3][+] , and 1.5 μg/L for Hg[2][+] . The linear response ranges were 10–500 µg/L for Cd[2][+] , As[3][+] , and Hg[2][+] , and 10–1000 µg/L for Pb²⁺. It is important to note that these performance metrics were obtained under controlled laboratory conditions. The complex compositions of real-world environmental samples can introduce significant interference, potentially compromising sensor sensitivity, selectivity, and accuracy. Therefore, further validation using authentic samples is imperative to assess its practical applicability. Chen et al. [43] fabricated a highly sensitive As³ ⁺ sensor by immobilizing a nanocomposite of cobalt ferrite (CoFe₂O₄), AuNPs, and ionic liquid (IL) on a glassy carbon electrode (GCE). Using square wave anodic stripping voltammetry (SWASV), this modified electrode achieved a LOD of 0.22 μg/L for As³ with a linear response across 0–100 μg/L, demonstrating strong potential for arsenic monitoring. The sensor demonstrated a high accuracy (98.5 %) for detecting As[3][+] in soil extracts using the standard addition method, showing strong agreement with conventional liquid chromatography-atomic fluorescence spectrometry（LC-AFS）measurements. However, the narrow linear range may limit its application for samples with highly variable arsenic concentrations. In another innovative study, Wu et al. [44] functionalized a gold electrode with poly(3-aminophenylboronic acid)-gold nanocomposite (PAPBA-AuNPs) for Al³ ⁺ sensing. This platform achieved an exceptionally low LOD of 0.019 aM (0.51262 ag/L) and maintained a wide dynamic range from 0.1 aM to 10 μM (2.698 ag/L-269.8 μg/L). Spike recovery tests using the standard addition method in 105-fold diluted tap water and instant noodle samples yielded average recovery rates between 86.0 % and 127.4 %, with RSD between 2.3 % and 7.9 %. While these results ’ confirm the method s feasibility, the significant fluctuations in recovery rates indicate potential matrix interference and a need for improved selectivity and accuracy for reliable real-sample analysis. 

Platinum nanoparticles (PtNPs) constitute a critical class of metallic nanomaterials for electrochemical sensing applications. Similar to AuNPs, they exhibit high electrical conductivity, exceptional chemical stability, and large surface-to-volume ratios. However, PtNPs exhibit superior electrocatalytic performance that provides distinct analytical advantages [45]. Notably, PtNPs maintain exceptional operational stability under harsh conditions, including strongly acidic environments 

3 

> _J. Liu et al.                                                                                                                                                                                                                                       International Journal of Electrochemical Science 20 (2025) 101209_ 

## **Table 1** 

Electrode Fabrication Techniques and Their Characteristics. 

|Electrode Fabrication|Characteristics|Limitations|
|---|---|---|
|Technology|||
|Drop Casting|Operational simplicity;<br>Rapid processing;|Non-uniform flm<br>formation;|
||Low equipment|Poor thickness control;|
||requirements;<br>Excellent for proof-of-<br>concept|Weak substrate adhesion,<br>leading to flm peeling,<br>poor reproducibility, and|
|||limited long-term|
|||stability;<br>Unsuitable for feld-<br>deployable or wearable<br>applications|
|Electropolymerization|Precise thickness|Stringent control|
||control via deposition|required for process|
||charge;|parameters (e.g.,|
||Strong adhesion and|potential/pH);|
||excellent stability;<br>Tailorable|Potential batch-to-batch<br>variations|
||functionality via||
||monomer selection for||
|Electrochemical Deposition|enhanced selectivity<br>Produces nano-flms<br>with high specifc|Requires precise control<br>of deposition parameters;|
||surface area and<br>porosity;|The toxicity of some<br>metals (e.g., Hg) limits|
||Abundant active sites<br>for signifcantly<br>enhanced sensitivity;<br>Excellent conductivity<br>and adhesion of the|their use|
||deposited layer||
|Self-assembled Monolayer|Forms well-ordered,|Stringent requirements|
|(SAM) Technology|defect-minimized<br>ultrathin flms;<br>Tunable interface|for preparation<br>conditions (environment,<br>substrate cleanliness);|
||properties with high|Limited mechanical|
||anti-interference|stability and robustness|
||capability;<br>Precise immobilization<br>of recognition<br>molecules via terminal|in complex media|
||groups||
|Advanced Film Formation|Enables large-area,|Dependency on|
|Techniques (e.g., Spin<br>Coating, Spray Coating)|uniform, and highly<br>reproducible flms;<br>Ideal for batch and|dedicated equipment;<br>Potential for low<br>material utilization|
||standardized sensor||
||manufacturing;||
||Spray coating allows<br>patterned printing on<br>fexible substrates for||
||wearables||



and elevated temperatures, and demonstrate enhanced resistance to interference in complex matrices such as biological fluids and food samples [46]. These attributes make PtNPs particularly suitable for applications in environmental monitoring, biomolecular detection, and food safety evaluation [47]. Recent advances in electrochemical sensors using PTNPs have demonstrated remarkable performance in heavy metal detection. Ru et al. [48] engineered a sensitive As³ ⁺ sensor by integrating octahedral UiO-67 MOFs with PtNPs, achieving a LOD of 0.48 nM (0.035 μg/L) and a linear range of 2.7–33.4 nM (0.202–2.502 μg/L). Although these findings are promising, the experiments were conducted under controlled laboratory conditions, and validation in real environmental water samples is still required. Elamin et al. [49] fabricated a PtNP-modified screen-printed electrode capable of simultaneously analyzing Cu²⁺, Zn²⁺, Hg²⁺, and Pb²⁺ in aqueous solution. The platform achieved LODs of 9.6, 1.9, 0.9, and 4.2 μg/L, – respectively, with recovery rates of 95 110 % in real water samples, confirming strong applicability. Wang et al. [50] designed an electrochemical sensor by functionalizing a GCE with a composite of graphene oxide GO, UiO-67, and PtNPs. The sensor demonstrated excellent sensitivity toward As[3] ,[+] achieving a LOD of 0.42 nM (0.031 μg/L) and a linear range of 2.7–40 nM (0.202–2.996 μg/L). The sensor’s high accuracy was confirmed in real-sample analysis, with an RSD below 5 %. AgNPs represent another significant metallic material for electrochemical sensor modification. While AgNPs share beneficial properties with AuNPs and PtNPs, such as high catalytic activity and optical properties, they are particularly notable for their superior costeffectiveness. A primary limitation of their widespread use is lower chemical stability, particularly a susceptibility to oxidize [51,52]. Yulirohyami et al. [53] developed a highly sensitive Hg²⁺ sensor by – immobilizing a silver nanoparticle dithizone@chitosan composite on a screen-printed electrode. This sensor achieved an impressive LOD of 0.06 μg/L for Hg²⁺ with a linear range of 1–5 μg/L. In real wastewater analysis, it demonstrated high reproducibility with an RSD of 1.71 %. Ajdari et al. [54] designed an electrochemical sensor by modifying a GCE with a composite of multi-walled carbon nanotubes (MWCNTs), p-aminothiophenol (PATP), and AgNPs (MWCNTs-PATP@AgNPs). This platform enabled the simultaneous detection of Pb²⁺ and Cd²⁺, achieving LODs of 0.125 nM (0.025 μg/L) and 1.47 nM (0.165 μg/L), respectively. The linear detection ranges were 0.5–60 nM (0.103–12.432 μg/L) for Pb²⁺ and 8–50 nM (0.899–5.62 μg/L) for Cd²⁺. It is important to note that these analytical figures were obtained under controlled laboratory conditions; validation with real environmental water samples is necessary to confirm practical accuracy. 

Additionally, Table 3 provides a systematic performance comparison of electrochemical sensors modified with representative metallic nanoparticles discussed in this section. 

## _3.1.2. Metal oxides_ 

## **Table 2** 

Characteristics of Inorganic Nanomaterial-Modified Electrochemical Sensors. 

|Modifcation Material<br>Metallic|Characteristics<br>Strong electron<br>transfer capability;<br>High mechanical<br>strength;|Limitations<br>Susceptible to oxidation;<br>High cost|
|---|---|---|
||High catalytic<br>effciency||
|Metal Oxide|Chemically stable|Complex preparation|
|Carbon-based inorganic<br>nanomaterials/graphene|Chemically stable;<br>High surface-to-<br>volume ratio;<br>High effciency in|process<br>Relatively high LODs<br>Inconsistent accuracy|
||electron transfer||



Metal oxide nanomaterials are now exceptionally suitable for the electrochemical sensing of heavy metals due to their distinct electronic characteristics and efficient electron transfer kinetics [55,56]. Extensive research has demonstrated that electrode modification with these nanoparticles significantly enhances sensor performance, improving both selectivity and sensitivity. Commonly investigated metal oxides include iron oxides (Fe₃O₄, α-Fe₂O₃), silver oxide (Ag₂O), zinc oxide (ZnO), manganese dioxide (MnO₂), and nickel oxide (NiO) [57–59]. 

Fe₃O₄ nanoparticles (Fe₃O₄NPs) are a predominant metal oxide nanomaterial in electrochemical heavy metal detection owing to their eco-friendly nature, cost-effectiveness, and wide availability [60,61]. Recent advances in nanocomposite-modified electrochemical sensors have demonstrated remarkable sensitivity for the identification of heavy metals. Zhang et al. [62] developed a sensitive detection platform by immobilizing Fe₃O₄@SiO₂-NH₂ nanocomposites onto a GCE. The modified sensor exhibited excellent performance for simultaneous quantification of Pb²⁺ and Hg²⁺, achieving LODs of 6.06 nM (1.255 μg/L) for Pb²⁺ and 9.09 nM (1.823 μg/L) for Hg²⁺, with wide linear ranges of 

4 

> _J. Liu et al.                                                                                                                                                                                                                                       International Journal of Electrochemical Science 20 (2025) 101209_ 

**Table 3** 

Performances of Metallic Nanoparticle-Modified Electrochemical Sensors. 

|Metallic Nanoparticle Modifcation|Detected Heavy Metal|Detection|Detection|Linear Range|Sample Recoveries|References|
|---|---|---|---|---|---|---|
|Materials|Ions|Methods|Limits|(μg/L)|(%)||
||||(μg/L)||||
|AuNPs|Pb²⁺, Cu²⁺, Hg²⁺|DPASV|0.07 (Pb²⁺)|1–1300|94.63–110.5 (Pb²⁺)|[41]|
||||0.13 (Cu²⁺)||91.4–110.93 (Cu²⁺)||
||||0.21 (Hg²⁺)||99.0–109.86 (Hg²⁺)||
|AuNPs|Pb²⁺, Cd²⁺, As3+, Hg2+|DPASV|4.4 (Pb²⁺)|10–1000 (Pb²⁺)|94.1–100.23 (Pb²⁺)|[42]|
||||9.4 (Cd²⁺)|10–500 (Cd²⁺)|95.42–102.38 (Cd²⁺)||
||||7.6 (As3+)|10–500 (As3+)|106.61–119.33 (As3+)||
||||1.5 (Hg²⁺)|10–500 (Hg²⁺)|118.35–150.22 (Hg²⁺)||
|AuNPs|As3+|SWASV|0.22|0–100|Unreported|[43]|
|PtNPs|As3+|SWASV|0.035|0.202–2.502|91.5–104.9|[48]|
|PtNPs|Pb²⁺, Cu²⁺, Zn2+, Hg2+|DPASV|4.2 (Pb²⁺)|5–300 (Pb²⁺)|98.5–112.22 (Pb²⁺)|[49]|
||||9.6 (Cu²⁺)|10–300 (Cu²⁺)|83.8–109.33 (Cu²⁺)||
||||1.9 (Zn2+)|2–150 (Zn2+)|93.5–101.11 (Zn2+)||
||||0.9 (Hg²⁺)|1–200 (Hg²⁺)|95–103.75 (Hg²⁺)||
|PtNPs|As3+|SWASV|0.031|0.202–2.996|91.8–108.9|[50]|
|AgNPs|Hg2+|SWASV|0.06|1–5|98.13|[53]|
|AgNPs|Pb²⁺, Cd²⁺|SWASV|0.025 (Pb²⁺)|0.103–12.432 (Pb²⁺)|96–104 (Pb²⁺)|[54]|
||||0.165 (Cd²⁺)|0.899–5.62 (Cd²⁺)|95.6–106.4 (Cd²⁺)||



0.02–100 μM (4.144–20720 μg/L) and 0.03–50 μM (6.018–10030 μg/L), respectively. Although designed for Pb²⁺ and Hg²⁺ detection in milk, its practical applicability is constrained by the fact that contamination of milk with these particular heavy metals is rare. Consequently, the sensor’s utility would be better suited for applications in matrices where such contamination is prevalent. Singh et al. [63] ₂O₃ and engineered a screen-printed electrode modified with Fe CS/ε-Fe₂O₃ nanocomposites for the simultaneous detection of Hg²⁺, Cd²⁺, and Pb²⁺ using electrochemical impedance spectroscopy (EIS). The sensor achieved LODs of 0.191 μM (38.314 μg/L) for Hg[2][+] , 0.167 μM (18.77 μg/L) for Cd[2][+] , and 0.177 μM (36.674 μg/L) for Pb[2][+] , across a 2–20 μM linear range for all three ions. In real water samples, recovery rates ranged from 107 to 113 % for Cd²⁺, 114–135 % for Hg²⁺, and 112–138 % for Pb²⁺. These elevated recovery rates, consistently exceeding 100 %, suggest a systematic positive bias, indicating a tendency for overestimation that must be addressed for reliable quantitative analysis. Doloi et al. [64] constructed a metal-organic framework (MOF)-based sensor integrated with Ag₂O nanoparticles for detecting Hg²⁺ and Cd²⁺ in water, achieving ultra-low LOD of 0.003 μM (0.601 μg/L) and 0.008 μM (0.899 μg/L), respectively. However, the sensor’ s performance in real water samples was not significant, indicating a critical need for further validation with diverse authentic samples to assess its practical applicability. Liu et al. [65] engineered a GCE modified with a Fe₃O₄@TiO₂@NG@Au@ETBD composite for Pb²⁺ detection in water. The sensor achieved an exceptionally low LOD of – 0.75 pM (0.15 ng/L) with a wide linear range of 0.4 20,000 pM (0.08–4144 ng/L). The sensor demonstrated high accuracy in the analysis of river water and rainwater, with recovery rates ranging from 99.67 % to 101.83 % and 101.50–102.33 %, respectively. Chama et al. [66] developed a sensor by functionalizing a GCE with EDTA-coated ZnO/Ag nanocomposites (ZnO@EDTA-Ag) for Cu²⁺ detection, achieving an LOD of 7 nM (0.444 μg/L) and a linear range of 0.007–10 μM (0.444–635.5 μg/L). When applied to detect Cu²⁺ in avocado juice, apple juice, lemon juice, and pond water samples, the sensor demonstrated strong practicality with recovery rates between 98 % and 101 %. Iqra et al. [67] achieved exceptional limits for the simultaneous detection of Pb²⁺ and Cd²⁺ ₂ using an L-cysteine-modified Ag@MnO nanocomposite on a GCE. The sensor demonstrated LODs of 0.052 nM (0.01 μg/L) for Pb²⁺ and 0.065 nM (0.007 μg/L) for Cd²⁺, with a shared linear range of 0.005–0.1 μM. Saida et al. [68] developed an electrochemical sensing platform by depositing nickel oxide nanoparticles (NiO NPs) onto a carbon graphite electrode for Cu²⁺ detection using square-wave anodic stripping voltammetry (SWASV). The fabrication process involved the electrochemical deposition of nickel from a 0.1 M boric acid/nickel salt solution, followed by anodic oxidation in a 0.1 M 

NaOH solution to form NiO NPs. The optimized sensor demonstrated exceptional performance, with a linear range of 0–150 nM (0–9.532 μg/L) Cu²⁺, an ultra-low LOD of 3.83 nM (0.243 μg/L), and a high sensitivity of 226.13 μA⋅μM⁻¹ ⋅cm⁻². When applied to determine Cu²⁺ in source water from two local brands, the sensor achieved recovery rates of 97.5 %-103.6 %, demonstrating high accuracy and strong practical applicability. Further validation with a wider variety of real water matrices is recommended to confirm its robustness. 

Additionally, Table 4 provides a systematic performance comparison of the representative metal oxides-modified electrochemical sensors discussed in this section. 

_3.1.3. Carbon-based inorganic nanomaterials/graphene_ 

Unsupported nanomaterials have emerged as attractive modifiers for electrochemical sensors, offering enhanced sensitivity and superior antiinterference properties. This category includes carbon nanoparticles (CNPs), carbon nanotubes (CNTs), carbon nanofibers (CNFs), graphene (GR), graphene oxide (GO), and related carbon-based nanostructures [69]. 

CNPs are classified by size: particles smaller than 10 nm are designated as carbon dots (CDots), while larger particles (≥10 nm) are referred to as CNPs [70]. These quasi-spherical nanostructures, which typically possess an amorphous-to-nanocrystalline core, exhibit exceptional electron transfer properties. When incorporated into electrochemical sensors, CNPs/CDots significantly enhance detection sensitivity [71]. A notable application was demonstrated by Cantalapiedra et al. [72], who developed a sensitive Cu²⁺ sensor using a polystyrene sulfonate-carbon nanoparticle (PSS-CNP) composite modified graphite electrode. This platform achieved an impressive LOD of 0.11 μg/L for aqueous Cu²⁺. When tested on various real water samples, the sensor showed strong agreement with atomic absorption spectroscopy (AAS) results, with a relative error of less than 5 %, confirming its practical utility. 

CNTs are one-dimensional (1D) nanomaterials composed of sp²-hybridized carbon atoms arranged in rolled graphene sheets, forming hollow tubes with diameters of 1–100 nm. They are categorized as either single-walled (SWCNTs) or multi-walled (MWCNTs). SWCNTs consist of a single rolled graphene sheet, typically measuring 1–100 µm in length, while MWCNTs are composed of several concentrically rolled graphene layers with a common central axis and an interlayer spacing of 0.34 nm [73,74]. CNTs are widely employed as electrode modifiers due to their exceptional chemical stability, which enhances sensor selectivity by mitigating interference from other species [75]. A notable example of MWCNT application was demonstrated by Wei et al. [76], who developed an electrochemical sensing system modified with MWCNTs for the 

5 

> _J. Liu et al.                                                                                                                                                                                                                                       International Journal of Electrochemical Science 20 (2025) 101209_ 

## **Table 4** 

Performances of Metal Oxide-Modified Electrochemical Sensors. 

|Metal Oxide Modifcation Materials|Detected Heavy Metal Ions|Detection Methods|Detection Limits|Linear Range|Sample Recoveries|References|
|---|---|---|---|---|---|---|
||||(μg/L)|(μg/L)|(%)||
|Fe3O4|Pb²⁺, Hg2+|DPASV|1.255 (Pb²⁺)|4.144–20720 (Pb²⁺)|95.1–112 (Pb²⁺)|[60]|
||||1.823 (Hg²⁺)|6.018–10030 (Hg²⁺)|108–114 (Hg²⁺)||
|Fe2O3|Pb²⁺, Cd²⁺, Hg²⁺|EIS|36.674 (Pb²⁺)|414.4–4144 (Pb²⁺)|112–138 (Pb²⁺)|[63]|
||||18.77 (Cd²⁺)|224.8–2248 (Cd²⁺)|107–113 (Cd²⁺)||
||||38.314 (Hg²⁺)|401.2–4012 (Hg²⁺)|114–135 (Hg²⁺)||
|Ag2O|Cd²⁺, Hg²⁺|DPASV|0.899 (Cd²⁺)|1.124–224.8 (Cd²⁺)|81.36–101.4 (Cd²⁺)|[64]|
||||0.601 (Hg²⁺)|4.012–300.9 (Hg²⁺)|78.71–95.66 (Hg²⁺)||
|Fe3O4, TiO2|Pb²⁺|SWASV|0.00015|0.00008–4.144|99.67–110.17|[65]|
|ZnO|Cu²⁺|DPASV|0.444|0.444–635.5|98–103|[66]|
|MnO2|Pb²⁺, Cd²⁺|SWASV|0.01 (Pb²⁺)|1.036–20.72 (Pb²⁺)|105 (Pb²⁺)|[67]|
||||0.007 (Cd²⁺)|0.506–11.24 (Cd²⁺)|104 (Cd²⁺)||
|NiO|Cu²⁺|SWASV|0.243|0–9.532|97.5–103.6|[68]|



simultaneous detection of multiple heavy metals. The sensor exhibited remarkable sensitivity, achieving detection limits of 0.5698 μg/L for Cd, 0.4024 μg/L for Pb, and 0.2565 μg/L for Hg, with a linear response range of 5–100 μg/L for all three ions. When applied to real water samples from around Beijing, the sensor showed strong agreement with ICP-MS measurements, yielding a relative RSD of less than 7 %, which confirms its considerable potential for practical applications. 

CNFs constitute a unique class of quasi-1D carbon with structural characteristics intermediate between CNTs and carbon fibers [77]. These versatile materials have widespread applications across numerous fields, including nanocomposites, photocatalysis, energy devices, catalyst supports, filtration, drug delivery, tissue engineering, and sensors [78]. In electrochemical sensing, Zhang et al. [79] demonstrated the effectiveness of CNFs by constructing a hybrid platform of AuNP-decorated CNF nanocomposite on a GCE. This sensor enabled the simultaneous detection of Cd²⁺, Pb²⁺, and Cu²⁺ with uniform sensitivity, achieving a LOD of 0.1 μM for all three target ions. It is important to note that these results were obtained under controlled laboratory conditions; validation with complex environmental water samples is required to confirm the sensor’s practical accuracy and robustness. 

Graphene, a two-dimensional (2D) monolayer of sp²-hybridized carbon atoms arranged in a hexagonal lattice [80], has profoundly advanced electrochemical sensing since its isolation in 2004. Its exceptional properties, including outstanding electrical conductivity ( _>_ 64 mS/cm) and an ultra-large theoretical surface area (2630 m²/g), promote highly sensitive detection of heavy metal ions [81]. As an electrode modifier, graphene enhances sensor performance through multiple mechanisms: it increases electrochemical activity, widens the potential window, reduces surface resistance, improves electron transfer rates, and facilitates both analyte adsorption and electron exchange processes. These synergistic effects substantially strengthen sensor sensitivity and selectivity [82,83]. Owing to these advantages, has been widely employed as a modifier in heavy metal detection platforms. Yuan et al. [84] fabricated a graphene-modified electrode for the simultaneous quantification of Cd²⁺ and Pb²⁺ in aqueous solution. The sensor achieved remarkable LODs of 0.207 μg/L for Cd²⁺ and 0.41 μg/L for Pb²⁺, with a linear response across a 1–100 μg/L range for both ions. The sensor exhibited good accuracy in real-sample analysis, with recovery rates ranging from 95.3 % to 106.3 %. Chen et al. [85] fabricated an electrochemical sensor by modifying a screen-printed carbon electrode with a three-dimensional (3D) melamine-doped graphene oxide/MXene composite aerogel (3D MGMA). This platform enabled the simultaneous detection of Zn²⁺, Cd²⁺, and Pb²⁺, achieving LODs of 0.48 μg/L, 0.45 μg/L, and 0.29 μg/L, respectively, and a wide linear response range of 3–900 μg/L. When applied to real water samples, the sensor demonstrated satisfactory accuracy and practical utility, with recovery rates of 95.02 %–106.77 % for Zn²⁺, 95.74 %–103.9 % for Cd²⁺, and 94.18 %– 106.47 % for Pb²⁺. Manasi et al. [86] developed an electrochemical sensor based on EDTA-functionalized PANI-GO for Pb²⁺ detection in aqueous solution, which exhibited a detection limit of 2.766 μg/L and a 

linear range from 0 to 40 μg/L. It should be noted that these analytical figures were obtained under controlled laboratory conditions; validation with real environmental water samples is required to confirm the sensor’s practical accuracy. 

Additionally, Table 5 provides a systematic performance comparison of the representative carbon-based nanomaterial-modified electrochemical sensors discussed in this section. 

## _3.2. Organic modification materials_ 

Organic small molecules and polymers have emerged as highly effective modifiers for electrochemical sensors, primarily due to their intrinsic molecular recognition capabilities. Characteristic functional groups, such as esters, amides, and hydroxyl moieties, enable selective coordination with specific heavy metal ions through chelation or adsorption mechanisms. This targeted interaction not only promotes the pre-concentration of analytes at the electrode interface but also directly facilitates efficient signal transduction, thereby enhancing both sensitivity and selectivity [87,88]. This section reviews representative organic small molecules and polymers used in sensor modification with a focus on their application for detecting heavy metal ions in aqueous environments. Table 6 summarizes the key properties and analytical advantages of the resulting modified sensors. 

## _3.2.1. Organic small molecules_ 

Organic small molecules are frequently integrated with other nanomaterials to construct high-performance electrochemical sensors. For example, Lochab et al. [89] designed a sensing platform using a GCE modified with 3-amino-1,2,4-triazole-5-thiol-functionalized MWCNTs. This platform demonstrated excellent sensitivity for thallium ion (Tl⁺) detection, achieving a LOD of 1.26 μg/L and a linear quantitative range of 10–100 μg/L. When evaluated with real industrial water samples, the sensor showed high practical utility, with recovery rates exceeding 96 %. Li et al. [90] developed a sensing platform based on – tungsten-ethylenediamine (WOx EDA) nanocomposites deposited on a GCE. This system enabled highly sensitive Pb²⁺ detection, with a LOD of 3.2 nM (0.663 μg/L) and a linear range of 0.01–10 μM (2.072–2072 μg/L). 

Gayathri et al. [91] developed a hybrid sensor by integrating a Schiff base ligand (SBL), specifically N,N′-bis(salicylidene)-1,2-phenylenediamine (BSD), with MWCNTs. This modified electrode was highly sensitive for the simultaneous determination of Pb²⁺ and Hg²⁺ in aqueous samples using SWASV. The sensor achieved remarkably low LODs of 0.3 nM (0.062 μg/L) for Pb²⁺ and 0.6 nM (0.12 μg/L) for Hg²⁺. When validated with groundwater and lake water samples, the sensor demonstrated high accuracy, yielding recovery rates of 99–103 % for Pb²⁺ and 98–101 % for Hg²⁺, which were consistent with AAS measurements. Li et al. [92] constructed a sensor using an MOF [Co₂(L1) (TPA)₂]⋅DMA⋅3CH₃OH⋅H₂O (Co-LTPA), where L1 is a thiacalix [4]arene-based ligand and TPA is terephthalic acid, immobilized on a GCE. 

6 

> _J. Liu et al.                                                                                                                                                                                                                                       International Journal of Electrochemical Science 20 (2025) 101209_ 

**Table 5** 

Performances of Inorganic Carbon Nanomaterial-Modified Electrochemical Sensors. 

|Inorganic Carbon Nanomaterials|Detected Heavy Metal Ions|Detection Methods|Detection Limits|Linear Range|Sample Recoveries|References|
|---|---|---|---|---|---|---|
||||(μg/L)|(μg/L)|(%)||
|CNPs|Cu²⁺|DPASV|0.11|210|101–106|[72]|
|GR|Pb²⁺, Cd²⁺, Hg²⁺|DPASV|0.4024 (Pb²⁺)|5–100 (Pb²⁺)|103–109.2 (Pb²⁺)|[76]|
||||0.5698 (Cd²⁺)|5–100 (Cd²⁺)|95.6–110 (Cd²⁺)||
||||0.2565 (Hg²⁺)|5–100 (Hg²⁺)|100.8–107.2 (Hg²⁺)||
|CNFs|Pb²⁺, Cd²⁺, Cu²⁺|SWASV|20.72 (Pb²⁺)|20.72–207.2 (Pb²⁺)|Unreported|[79]|
||||11.24 (Cd²⁺)|11.24–112.4 (Cd²⁺)|||
||||6.355 (Cu²⁺)|6.355–63.55 (Cu²⁺)|||
|GR|Pb²⁺, Cd²⁺|DPASV|0.41 (Pb²⁺)|1–100 (Pb²⁺)|95.3–106.3 (Pb²⁺)|[84]|
||||0.207 (Cd²⁺)|1–100 (Cd²⁺)|97.8–107 (Cd²⁺)||
|GR|Pb²⁺, Cd²⁺, Zn²⁺|DPASV|0.29 (Pb²⁺)|3–900 (Pb²⁺)|96.27–105.57 (Pb²⁺)|[85]|
||||0.45 (Cd²⁺)|3–900 (Cd²⁺)|93.73–104.5 (Cd²⁺)||
||||0.48 (Zn²⁺)|3–900 (Zn²⁺)|94.18–106.47 (Zn²⁺)||
|GO|Pb²⁺|DPASV|2.766|0–40|Unreported|[86]|



## **Table 6** 

Summary of Key Characteristics of Organic Material-Modified Electrochemical Sensors. 

|<br>Sensors.|||
|---|---|---|
|Modifer Material|Characteristics|Limitations|
|Organic Small|Simple modifcation/|Signifcant variability in|
|Molecules|preparation process;|detection results;|
|Organic Polymers|Low cost<br>Wide linear range;|High detection limit;<br>Narrow linear range<br>Limited electron transfer|
|(MOFs, COFs)|Strong anti-interference|capability;|
||capability|High detection limit|



This Co-LTPA-modified sensor exhibited outstanding performance for detecting Cd²⁺ and Pb²⁺, achieving ultralow LODs of 0.119 nM (0.013 μg/L) and 0.279 nM (0.057 μg/L), respectively. The linear detection ranges were 0.01–6 μM (2.072–1243.2 μg/L) for Pb²⁺ and 0.08–5.8 μM (8.992–651.92 μg/L) for Cd²⁺. Application to various real-world samples resulted in excellent recovery rates of 99–101 % for Cd²⁺ and 98–102 % for Pb²⁺, with RSD between 1.7 % and 5.0 % and 1.9–4.0 %, respectively, confirming the sensor’s robustness and practical applicability for environmental monitoring. These results indicate the strong practical applicability of this method. 

For a systematic comparison, Table 7 summarizes the analytical performance of these and other representative electrochemical sensors modified with organic small molecules discussed in this section. 

## _3.2.2. Organic polymers_ 

Organic polymers are increasingly recognized as pivotal modifiers in electrochemical sensor design, particularly when integrated with inorganic nanomaterials to create hybrid sensing platforms. Such composites combine the conductivity and functional tunability of polymers with the structural and catalytic advantages of nanomaterials, resulting in improved sensitivity and selectivity, which are properties critical for environmental monitoring applications [93,94]. 

Ajdari et al. [95] developed a high-performance electrochemical sensor for the simultaneous detection of Pb²⁺ and Cd²⁺ by modifying a GCE with multi-walled carbon nanotube-polyethylene (MWCNT-PE) 

nanocomposites. The platform achieved remarkably low LODs of 0.125 nM (0.025 μg/L) for Pb²⁺ and 1.47 nM (0.165 μg/L) for Cd²⁺, with linear detection ranges of 0.5–60.0 nM (0.103–12.432 μg/L) and 8.0–50.0 nM (0.899–5.62 μg/L), respectively. Validation using real samples and comparison with ICP-MS yielded recovery rates of 95.6 %– 105.3 %, confirming its satisfactory accuracy. Maheshwaran et al. [96] synthesized a novel conductive polymer composite from dedoped polyaniline (PAni) with Reactive Yellow 42 dye (RYFG). The resulting PAni-RYFG composite exhibited unique electrochemical properties and was applied to heavy metal detection, achieving a LOD of 2 nM (0.401 μg/L) for Hg²⁺ and 6.2 nM (1.284 μg/L) for Pb²⁺. The sensor demonstrated a linear response across a concentration range of 1–21 μM. When tested on real water samples, it showed recovery rates of 100.2–105.0 % for Pb²⁺ and 92.3–98.4 % for Hg²⁺, indicating reasonable accuracy for environmental analysis. Maheshwaran et al. [97] developed a sensor based on a polyaniline composite incorporating a benzothiazole derivative, 3,5-bis(benzo[ _d_ ]thiazol-2-yl)-[1,1′-biphenyl] -4-ol, for the detection of Hg²⁺ and Pb²⁺. The sensor exhibited high sensitivity for Hg²⁺ and Pb²⁺ detection, achieving LODs of 1 nM (0.2 μg/L) for Hg²⁺ and 4.6 nM (0.953 μg/L) for Pb²⁺, with a linear range of 1–24.84 μM. Wu et al. [98] designed a molecularly imprinted sensor using a polyaniline-gold nanoparticle (PANI-AuNPs) nanocomposite for the detection of Cd²⁺. The molecular imprinting technique endowed the platform with selective binding sites for Cd²⁺, while AuNPs enhanced electrical conductivity and electron transfer. This sensor demonstrated a LOD of 1.2 μg/L and a linear range of 5–100 μg/L in boiled water samples. However, the enhanced performance was accompanied by increased manufacturing costs due to the incorporation of gold nanoparticles. In validation tests using tap water, lake water, and electroplating wastewater, the sensor achieved recovery rates of 96–103 %, confirming its broad applicability and robustness for complex real-world matrices. 

MOFs have gained significant attention for sensor development due to their exceptional metal-coordination properties and highly tunable porous structures, which are particularly advantageous for identifying heavy metal ions [99]. Chen et al. [100] developed an advanced sensing platform using NH₂-MIL-101(Fe)-modified GCE. The optimized sensor 

## **Table 7** 

Performances of Organic Small Molecule-Modified Electrochemical Sensors. 

|Organic Small Molecule Modifcation Materials|Detected Heavy|Detection|Detection|Linear Range|Sample Recoveries|References|
|---|---|---|---|---|---|---|
||Metal Ions|Methods|Limits|(μg/L)|(%)||
||||(μg/L)||||
|3-amino−1,2,4-triazole−5-thiol<br>Ethylenediamine, Nafon|Tl⁺<br>Pb²⁺|DPASV<br>SWASV|1.29<br>0.663|10–100<br>2.072–2072|96.9–98.1<br>95.4–107.1|[89]<br>[90]|
|N,N′-bis(salicylidene)−1,2-phenylenediamine|Pb²⁺, Hg²⁺|SWASV|0.062 (Pb²⁺)|0.414–32.116 (Pb²⁺)|99–101.3 (Pb²⁺)|[91]|
||||0.12 (Hg²⁺)|0.401–31.093 (Hg²⁺)|102.5–104 (Hg²⁺)||
|Thiacalix[4]arene, Terephthalic acid, N,|Pb²⁺, Cd²⁺|SWASV|0.057 (Pb²⁺)|2.072–1243.2 (Pb²⁺)|97.71–102.38 (Pb²⁺)|[92]|
|N’-dimethylacetamide|||0.013 (Cd²⁺)|8.992–651.92 (Cd²⁺)|98.82–101.17 (Cd²⁺)||



7 

> _J. Liu et al.                                                                                                                                                                                                                                       International Journal of Electrochemical Science 20 (2025) 101209_ 

exhibited outstanding multi-analyte detection capabilities for Pb²⁺, Cu²⁺, and Hg²⁺, achieving remarkably low LODs of 12.0 nM (2.486 μg/L), 8.53 nM (0.542 μg/L), and 18.0 nM (3.61 μg/L), respectively. The corresponding linear detection ranges were 0.1–10 μM (20.72–2072 μg/L) for Pb²⁺, 1.0–10 μM (63.55–635.5 μg/L) for Cu²⁺, and 1.0–12 μM (200.6–2407.2 μg/L) for Hg²⁺. Although the experiment was conducted under controlled laboratory conditions, its accuracy in complex, real environmental water samples requires further validation. Sun et al. [101] developed a high-performance sensor by decorating 2D Cu-MOFs with copper nanoparticles on ITO electrodes (Cu(NPs)/Cu-MOFs@ITO). This platform achieved a LOD of 0.065 μM (13.468 μg/L) for Pb²⁺ with a linear range of 4.8–50 μM (994.56–10360 μg/L). A 96 % recovery rate for Pb²⁺ in a seawater sample demonstrates the potential of the sensor for marine monitoring applications; however, comprehensive validation across a wider range of real water matrices is necessary to establish its accuracy and robustness. Zhang et al. [102] achieved exceptional sensitivity using a ZIF-67@antimonene-modified screen-printed electrode. The platform demonstrated ultra-trace detection capabilities for Cu²⁺, Pb²⁺, and Hg²⁺, with extremely low LOD of 0.01 pM (0.6355 pg/L), 0.042 pM (8.7024 pg/L), and 0.031 pM (6.2186 pg/L), respectively, and – a consistent linear range of 0.1 200 pM. The sensor exhibited high selectivity, as confirmed by excellent spike recovery rates of 94.9–108.1 % and a low RSD of less than 1.35 % in complex matrices such as milk, honey, and black tea. Liu et al. [103] developed an NH₂-MIL-53(Fe)@ITO sensor for Pb²⁺ detection. The sensor achieved a LOD of 0.1 μM (20.72 μg/L); however, it exhibited a relatively constrained linear range of 2–4 μM (414.4–828.8 μg/L). The experiment was conducted under controlled laboratory conditions, and its accuracy in real environmental water samples requires further validation. In a significant methodological advancement, Xiao et al. [104] developed an As³ ⁺ sensor by hydrothermally synthesizing Fe-MOF/MXene composites on a GCE. The sensor achieved a detection limit of 0.58 ng/L within a – linear quantification range of 10 100 ng/L. Testing in real water samples (tap water, river water, and lake water) demonstrated recovery rates of 97.4–98.4 % for As³ ⁺. These results, which were consistently slightly higher than those from ICP-MS analysis, indicate the need for validation with additional real samples to confirm accuracy. Zhang et al. [105] created a highly sensitive sensor using a Bi₂CuO₄@Al-MOF@UiO-67 hybrid nanocomposite on a screen-printed electrode. This platform enabled the simultaneous quantification of Cd²⁺, Cu²⁺, Pb²⁺, and Hg²⁺ ions in dairy products, achieving exceptional sensitivities with LODs of 0.02 pM (2.248 pg/L), 0.032 pM (2.0336 pg/L), 0.018 pM (3.7296 pg/L), and 0.041 pM (8.2246 pg/L), respectively, and uniform linear responses up to 60 pM. The sensor demonstrated practical utility, – achieving recovery rates of 90.00 99.00 % across multiple real samples. 

Zhang et al. [106] developed a sensor based on a CoFe₂O₄@C-600 magnetic composite for Pb²⁺ detection. The sensor demonstrated a remarkably low LOD of 0.0043 μM (0.89 μg/L) and an exceptionally broad linear response from 0.001 to 60 μM (0.2072–12432 μg/L). When applied to real samples of Yangtze River water and soil leachate, it achieved recovery rates of 98.20–112.40 % with RSD below 5 %. The results showed a negligible difference from the standard flame atomic absorption spectroscopy (FAAS) method, confirming its reasonable accuracy for environmental analysis. For clinical applications, Liu et al. [107] engineered a novel sensor using a 2D boat-like Co(II)-MOF to modify screen-printed electrodes. This sensor detected Hg²⁺ in urine samples with a detection limit of 15.09 nM (3.027 μg/L), operating –100 nM effectively within a linear quantification window of 50 (10.03–20.06 μg/L). The sensor achieved recovery rates of 92.80–107.99 % with an RSD below 4.38 % in authentic urine samples. Furthermore, the results showed excellent agreement with those from atomic fluorescence spectroscopy (AFS), validating the proposed electrochemical sensing approach for detecting Hg²⁺ in clinical matrices. Liang et al. [108] made significant progress in multi-analyte detection by developing a Fe@YAU-101 modified GCE for the simultaneous detection of Hg²⁺, Pb²⁺, and Cd²⁺. The sensor demonstrated exceptional 

sensitivity, achieving LODs of 66.7 pM (7.497 ng/L) for Cd²⁺, 53.3 pM (11.043 ng/L) for Pb²⁺, and 13.3 pM (2.667 ng/L) for Hg²⁺. When applied to drinking water, the sensor achieved recovery rates of 99.6–100.4 %, demonstrating high accuracy. However, further validation with a broader range of real water samples is recommended to confirm its practical utility. Gajanan et al. [109] developed an electrochemical sensor using an Ag/SWNTs@CuBTC-MOF composite for the simultaneous detection of Fe³ ⁺, Hg²⁺, and Ni²⁺ in water. The sensor demonstrated detection limits of 0.169 μg/L for Fe³ ⁺, 0.278 μg/L for Hg²⁺, and 0.152 μg/L for Ni²⁺, with corresponding linear ranges of 0.055–0.558 μg/L, 0.2–2.006 μg/L, and 0.058–0.586 μg/L, respectively. Although the platform demonstrated strong analytical performance under controlled laboratory conditions, its accuracy in real environmental water samples requires further validation. Kamlesh et al. [110] developed an electrochemical sensor based on an EDTA-functionalized AgNPs/UIO-66 composite (EDTA@AgNP’s_UIO-66) for detecting Hg²⁺ in aqueous solutions. The sensor achieved a detection limit of 0.038 μg/L and a linear range of 2.006–22.066 μg/L for Hg²⁺. In the spike-and-recovery tests using three different real water samples, it demonstrated good accuracy and reliability, with recovery rates of 89.3 %–95.4 % and RSD below 4.1 %. To establish its broad applicability, further testing with a wider variety of real environmental samples is recommended. 

Building on the success of MOFs, covalent organic frameworks (COFs) have emerged as promising platforms for detecting metallic species due to their exceptional metal-coordinating functionalities and highly tunable porous architectures. Zahra et al. [111] demonstrated this potential by developing an advanced electrochemical platform that integrates a melamine-trimesic acid COF with carbon black (CB) on a GCE. Using differential pulse anodic stripping voltammetry (DPASV), the sensor simultaneously detected Zn²⁺, Cd²⁺, Pb²⁺, and Hg²⁺ ions. It ⁺ achieved remarkably low LODs of 0.003 nM (0.1 ng/L) for Zn² , 0.002 nM (0.2 ng/L) for Cd²⁺, 0.001 nM (0.2 ng/L) for Pb²⁺, and 0.0003 nM (0.06 ng/L) for Hg²⁺. The corresponding linear detection ranges were 0.009–1100 nM (0.0005–71.918 μg/L) for Zn²⁺, 0.005–1100 nM (0.0005–123.64 μg/L) for Cd²⁺, 0.003–1100 nM (0.0006–227.92 μg/L) for Pb²⁺, and 0.001–1100 nM (0.0002–220.66 μg/L) for Hg²⁺. When evaluated with multiple real samples, the sensor achieved recovery rates of 98.8 %–104.2 % and an RSD below 3.1 %. The results showed good agreement with AAS, confirming the sensor’s practical utility for reliable environmental monitoring. Mohammad et al. [112] further demonstrated the capabilities of COF by developing a sensor based on a triazine-based framework. The sensor achieved detection limits of 1.1 nM (0.227 μg/L) for Pb²⁺ and 1.8 nM (0.202 μg/L) for Cd²⁺, with corresponding linear ranges of 1.0–110.0 nM (0.207–22.792 μg/L) and 5.0–300.0 nM (0.562–33.72 μg/L), underscoring the high affinity of nitrogen-rich COF structures for heavy metal coordination. In an innovative approach that combines organic and polymeric components, Guo et al. [113] developed a composite sensor from a chitosan-functionalized COF embedded with poly(3,4-ethylenedioxythiophene):polystyrene sulfonate (PEDOT: PSS), designated as CS/COFs. This sensor detected Cd²⁺ with a LOD of 13.8 ng/L and a linear range of 400–2400 μg/L. While the sensor demonstrated promising analytical performance, its fabrication involved a relatively complex synthesis process. In validation tests using the centrifugate of a scallop washing solution, the sensor achieved recovery rates of 97.77–102.69 % with an RSD between 1.83 % and 2.00 %. To establish its accuracy and practical utility, further testing in a wider variety of real water samples is recommended. 

Zhang et al. [114] developed a novel detection platform based on a thiophene-functionalized COF, synthesized by condensing [2,2′-bithiophene]-5,5′-dicarbaldehyde (BTDC) and 4,4′-diamino-*p*-terphenyl (TAP). This sensor achieved exceptional sensitivity for the dual detection of Pb²⁺ and As⁵⁺, with LODs of 0.035 μg/L and 0.42 μg/L, respectively. It demonstrated an impressive linear response across three orders of magnitude, specifically 0.5–1000 μg/L for Pb²⁺ and 25–10000 μg/L 

8 

_International Journal of Electrochemical Science 20 (2025) 101209_ 

> _J. Liu et al.                                                                                                                                                                                                                                       International Journal Electrochemical_ 

for As⁵⁺. In applications with seawater, industrial wastewater, and tap water, the sensor demonstrated good accuracy and practical utility, achieving recovery rates of 97.5–106.1 % for Pb²⁺ and 95.7–105.3 % for As⁵⁺. Yu et al. [115] developed an innovative paper-based analytical device integrated with a hybrid nanocomposite of a COF (COFDPTB), gold nanoparticles (AuNPs), and graphene (GR). The COFDPTB structure was synthesized via Schiff-base condensation of 2,5-dimethoxyterephthalaldehyde and 1,3,5-tris(4-aminophenyl)benzene. This multicomponent sensor was applied for the simultaneous detection of Cd²⁺, Pb²⁺, and Cu²⁺ ⁺ in Chinese liquor, achieving LODs of 3.025 nM (0.34 μg/L) for Cd² , ⁺ ⁺ 5.849 nM (1.211 μg/L) for Pb² , and 9.993 nM (0.635 μg/L) for Cu² . The sensor exhibited wide linear dynamic ranges of 0.5–18 μM (56.2–2023.2 μg/L) for Cd²⁺, 0.5–6.0 μM (103.6–1243.2 μg/L) for Pb²⁺, and 0.5–6.0 μM (31.775–381.3 μg/L) for Cu²⁺. Analysis of three different Chinese liquor samples yielded recovery rates of 94.2–94.6 % for Cd²⁺, 96.4–101.4 % for Pb²⁺, and 94.4–102.8 % for Cu²⁺. These re’ sults confirm the sensor s reasonable accuracy for this specific application; however, further validation with a broader array of sample matrices is recommended to fully establish its general practical utility. 

Additionally, Table 8 provides a systematic comparison of the analytical performance for the representative organic polymer-modified electrochemical sensors discussed in this section. 

## _3.3. Biomaterials_ 

Biomaterials, including nucleic acids, enzymes, antigens/antibodies, and whole cells, have gained prominence as recognition elements in electrochemical sensing because of their intrinsic molecular specificity [116]. These biocomponents provide highly selective binding affinities 

for specific heavy-metal ions, facilitating accurate detection even in complex environmental matrices [117]. The fundamental detection mechanism relies on the specific capture of a target ion by the biomaterial, which generates a quantifiable change in the electrochemical signal at the biofunctionalized electrode interface. These signal variations, such as alterations in interfacial electron transfer resistance, modulation of catalytic current, or shifts in electrochemical impedance, provide an indirect yet highly specific method for quantifying heavy metal concentrations [118]. For instance, functional nucleic acids, such as metal-specific aptamers and DNAzymes, undergo conformational changes upon ion binding, which modulate electron transfer pathways. – In contrast, heavy metal sensitive enzymes, such as certain oxidoreductases, experience activity inhibition, resulting in measurable current variations. These attributes, combined with inherent capacity for signal amplification, establish biomaterial-modified sensors as promising platforms for advanced environmental monitoring and toxicological assessment [119]. The key analytical characteristics of the 

**Table 9** 

Characteristics of Biomaterial-Modified Electrochemical Sensors. 

||Modifer|Characteristics|Limitations|
|---|---|---|---|
||Material|||
||DNA|Low detection limits;|Narrow linear range;|
|||High selectivity;|Stringent environmental|
|||Designable|requirements;|
||Enzymes|sequences<br>Low detection limits;<br>Strong stability;<br>High selectivity|Poor storage stability<br>Narrow linear range;<br>Limited variety;<br>High cost; Complex preparation|



**Table 8** 

Performances of Organic Polymer-Modified Electrochemical Sensors. 

|Organic Polymer Modifcation|Detected Heavy Metal|Detection|Detection|Linear Range|Sample Recoveries|Sample Recoveries|References|
|---|---|---|---|---|---|---|---|
|Materials|Ions|Methods|Limits|(μg/L)|(%)|||
||||(μg/L)|||||
|Poly|Pb²⁺, Cd²⁺|SWASV|0.025 (Pb²⁺)|0.103–12.432 (Pb²⁺)|96–104.7 (Pb²⁺)||[95]|
|(2-aminothiophenol)|||0.165 (Cd²⁺)|0.899–5.62 (Cd²⁺)|95.6–106.4|(Cd²⁺)||
|Polyaniline|Pb²⁺, Hg²⁺|DPASV|1.284 (Pb²⁺)|207.2–4351.2 (Pb²⁺)||92.3–103 (Pb²⁺)|[96]|
||||0.401 (Hg²⁺)|200.6–4212.6 (Hg²⁺)|96.6–105 (Hg²⁺)|||
|Polyaniline-benzothiazole|Pb²⁺, Hg²⁺|DPASV|0.953 (Pb²⁺)|207.2–5146.848 (Pb²⁺)|91–104 (Pb²⁺)||[97]|
||||0.2 (Hg²⁺)|200.6–4982.904 (Hg²⁺)|90–103.6 (Hg²⁺)|||
|Polyaniline|Cd²⁺|DPASV|1.2|5–100|96–103||[98]|
|MOF|Pb²⁺, Cu²⁺, Hg²⁺|DPASV|2.486 (Pb²⁺)|20.72–2072 (Pb²⁺)||98.84–103.33|[100]|
|(NH₂-MIL−101(Fe))|||0.542 (Cu²⁺)|63.55–635.5 (Cu²⁺)||||
||||3.61 (Hg²⁺)|200.6–2407.2 (Hg²⁺)||||
|MOF|Pb²⁺|SWASV|13.468|994.56–10360|96||[101]|
|(Cu-MOFs)||||||||
|MOF|Pb²⁺|SWASV|20.72|414.4–828.8|Unreported||[103]|
|(NH₂-MIL−53(Fe))||||||||
|MOF|As3+|SWASV|0.00058|0.001–0.1||97.4–98.4|[104]|
|(Fe-MOF/MXene)||||||||
|MOF|Pb²⁺|DPASV|0.89|0.2072–12432||98.2–112.4|[106]|
|(CoFe2O4@C−600)||||||||
|MOF|Hg²⁺|DPASV|0.038|2.006–22.066||89.3–95.4|[109]|
|(UIO−66)||||||||
|MOF|Fe3⁺, Hg²⁺, Ni²⁺|DPASV|0.169 (Fe3⁺)|0.055–0.558 (Fe3⁺)|Unreported||[110]|
|(CuBTC MOF)|||0.278 (Hg²⁺)|0.2–2.006 (Hg²⁺)||||
||||0.152 (Ni²⁺)|0.058–0.586 (Ni²⁺)||||
|COF|Pb²⁺, Cd²⁺, Zn2+, Hg2+|DPASV|0.0002 (Pb²⁺)|0.0006–227.92 (Pb²⁺)||99.7–104.2 (Pb²⁺)|[111]|
|(CB-COF)|||0.0002 (Cd²⁺)|0.0005–123.64 (Cd²⁺)|98.8–100.9|(Cd²⁺)||
||||0.0001 (Zn2+)|0.0005–71.918 (Zn2+)|99.6–101.9|(Zn2+)||
||||0.00006 (Hg²⁺)|0.0002–220.66 (Hg²⁺)|99.8–101.6|(Hg²⁺)||
|COF|Pb²⁺, Cd²⁺|SWASV|0.227 (Pb²⁺)|0.207–22.792 (Pb²⁺)|Unreported||[112]|
|(TPT-COF)|||0.202 (Cd²⁺)|0.562–33.72 (Cd²⁺)||||
|COF|Cd²⁺|DPASV|0.0138|400–2400||97.77–102.69|[113]|
|(CS/COFs)||||||||
|COF|Pb²⁺, As5+|DPASV|0.035 (Pb²⁺)|0.5–1000 (Pb²⁺)||97.51–106.07 (Pb²⁺)|[114]|
|(Ta-BTDC-COF)|||0.42 (As5+)|25–10000 (As5+)|95.69–105.31 (As5+)|||
|COF|Pb²⁺, Cd²⁺, Cu²⁺|DPASV|1.211 (Pb²⁺)|103.6–1243.2 (Pb²⁺)||96.4–101.4 (Pb²⁺)|[115]|
|(COFDPTB)|||0.34 (Cd²⁺)|56.2–2023.2 (Cd²⁺)|94.2–94.6 (Cd²⁺)|||
||||0.635 (Cu²⁺)|31.775–381.3 (Cu²⁺)|94.4–102.8|(Cu²⁺)||



9 

> _J. Liu et al.                                                                                                                                                                                                                                       International Journal of Electrochemical Science 20 (2025) 101209_ 

biomaterial-based sensors discussed are systematically compared in Table 9. 

## _3.3.1. Functional nucleic acids_ 

Nucleic acids are highly promising for electrochemical sensing due to their unique metal-coordinating capabilities, which enable the formation of selective complexes such as thymine-Hg²[+] -thymine (T-Hg[2][+] -T) and cytosine-Ag⁺-cytosine (C-Ag[+] -C) [120]. These specific interactions form the basis for developing highly selective electrochemical sensors [121]. Among functional nucleic acids (FNAs), DNAzymes and aptamers serve as particularly effective biorecognition elements. DNAzymes offer distinct advantages for sensing applications, including exceptional thermostability and high binding specificity for target heavy metal ions [122]. A significant advancement was demonstrated by Song et al. [123], who developed an ultrasensitive platform for Pb²⁺ detection by immobilizing DNAzymes on a Fe/ZIF-8 nanocomposite. The sensor achieved exceptional performance, with a remarkably low LOD of 0.1 pM (0.02 ng/L) and a broad linear range from 0.005 to 50,000 nM (1.036–10360000 ng/L). It also exhibited strong anti-interference capability and high selectivity for Pb²⁺ even in complex aqueous matrices. While these results are promising, the accuracy of the sensor in real environmental water samples requires further validation, as the study was conducted under controlled laboratory conditions. 

Aptamers, comprising single-stranded DNA (ssDNA), RNA, or peptide sequences, demonstrate high binding affinity and selectivity for specific heavy metal ions [124]. These synthetic oligonucleotides serve as cost-effective alternatives to antibodies, offering superior stability and simpler synthesis while maintaining high specificity [125]. Recent advances have successfully integrated these biorecognition elements into electrochemical detection platforms. For instance, Dong et al. [126] developed an advanced detection platform by modifying gold electrodes with a nanocomposite of platinum nanoparticles embedded in a copper-based metal-organic framework (PtNPs@Cu-MOF), which was further functionalized with DNA walkers. This configuration achieved ultra-sensitive Pb²⁺ detection, with a LOD of 0.2 pM (0.041 ng/L) and a linear range spanning 0.003–5000 nM (0.621–1036000 ng/L). In validation tests, the sensor detected Pb²⁺ in tap water and orange juice, achieving recovery rates of 110.0–110.5 % and 89.7–100.2 %, respectively. The elevated recovery in tap water suggests potential matrix effects; therefore, validation across a more diverse set of real-world samples is essential to confirm its accuracy and practical applicability. Zhu et al. [127] developed a sensor using gold nanostructures conjugated with engineered DNA sequences (S1 fragments) for Hg²⁺ detection, achieving a LOD of 8.5 pM (1.705 ng/L). Despite this high sensitivity, the platform’s practical application was limited by a relatively narrow linear range of 5–5000 nM (1003–1003000 ng/L) and a complex fabrication process. When evaluated in tap water, river water, and medical wastewater, the sensor demonstrated recovery rates of 98.3 %–105.2 %, confirming its potential utility for real-sample analysis. Li et al. [128] functionalized a carboxylated graphene oxide (GO− COOH) electrode with DNA oligonucleotides for Hg²⁺ detection. The sensor achieved a detection limit of 10 pM (2.006 ng/L); however, its practical utility is – constrained by a very restricted linear range of 10 25 pM (2.006–5.015 ng/L). Wang et al. [129] designed a sensor based on a UiO-66-CNT composite functionalized with guanine-rich (G-rich) and thymine-rich (T-rich) oligonucleotides for the simultaneous detection of Pb²⁺ and Hg²⁺. The detection mechanism relies on the formation of G-Pb²⁺-G and T-Hg²⁺-T complexes, which induce distinct voltammetric peak shifts. The sensor achieved LODs of 9.65 nM (2000 ng/L) for Pb²⁺ and 2.49 nM (500 ng/L) for Hg²⁺, with corresponding linear ranges of 24.1–4820 nM (5000–1000000 ng/L) and 4.98–4980 nM (1000–1000000 ng/L). Application to real food, water, and soil samples demonstrated good accuracy and practical utility, with recovery rates of 94.89 %–101.70 % for Pb²⁺ and 97.74 %–101.70 % for Hg²⁺. 

In a recent study, Jin et al. [130] developed an innovative biosensing platform for Pb²⁺ detection using AuNP-modified GCE functionalized 

with guanine-rich Y-shaped DNA sequences. The sensor demonstrated excellent analytical performance for Pb²⁺ quantification in complex matrices such as beverages and municipal water, achieving a LOD of 0.38 nM (78.736 ng/L) and a linear range of 0.5–1000 nM (103.6–207200 ng/L). Validation in tap water and tea samples yielded average recovery rates of 92.0–116.3 % and 101.6–116.0 %, respectively, with RSD values below 12 %; these results indicate good precision but suggest potential for improved accuracy in future iterations. In another study, Wang et al. [131] engineered a hierarchical nanocomposite sensor by integrating thymine-rich DNA fragments with a chitosan/GO/MoS₂/AuNPs modified electrode for Hg²⁺ detection. This multicomponent design achieved exceptional sensitivity with an LOD of – 5.8 ng/L and a linear range of 10 4000 ng/L, which is highly relevant for environmental monitoring. However, the sensor showed variable accuracy, with average recovery rates ranging from 80.87 % to 127.92 % in tap water. Consequently, validation across a broader spectrum of real water samples is recommended to establish its reliability for practical applications. 

Additionally, Table 10 provides a systematic comparison of the analytical performance for the representative functional nucleic acidbased electrochemical sensors discussed in this section. 

## _3.3.2. Enzymes_ 

Enzymes function as highly effective biorecognition elements in electrochemical sensing due to their specific catalytic activity and selective interactions with heavy metal ions at their active sites [132]. In these biosensing platforms, the selective binding of a target metal ion to the enzyme modulates its catalytic activity. This modulation, in turn, generates a quantifiable change in the electrochemical signal, such as a shift in current, potential, or impedance, enabling the indirect but highly specific quantification of the heavy metal analytes [133]. 

Gumpu et al. [134] designed a dual-analyte electrochemical biosensor by co-immobilizing urease and cerium oxide (CeO₂) nanoparticles within a semi-permeable membrane on a platinum electrode. The resulting Pt/CeO₂/urease biosensor achieved simultaneous detection of Pb²⁺ and Hg²⁺ in aqueous samples by measuring the differential inhibition of urease activity. It demonstrated a linear range of 500–2200 nM (103600–455840 ng/L) for Pb²⁺ and 20–800 nM (4012–160480 ng/L) for Hg²⁺, with corresponding LODs of 19 nM (3936.8 ng/L) and 18 nM (3610.8 ng/L). Although these results highlight the platform’s strong analytical performance, the experiments were conducted under controlled laboratory conditions; further validation in real environmental water samples is needed to establish practical applicability. Magar et al. [135] proposed an alternative enzyme-inhibition strategy using choline oxidase (ChOx) for Pb²⁺ detection. Their system incorporated cerium oxide-functionalized MWCNT on a glassy carbon surface to enhance catalytic and electrochemical activity. In this setup, ChOx catalyzes the oxidation of choline to betaine, while Pb²⁺ ions selectively inhibit ChOx, thereby suppressing enzymatic oxidation and yielding measurable electrochemical signals. This sensor achieved remarkable sensitivity, with an LOD of 0.04 nM (8.288 ng/L) across a linear range of 0.1–1.0 nM (20.72–207.2 ng/L). 

Additionally, Table 11 provides a systematic comparison of the key analytical performance metrics for the representative enzyme-modified electrochemical sensors discussed in this section. 

## **4. Machine learning algorithms** 

The practical application of electrochemical sensors for heavy metal ion detection faces significant challenges due to signal interference from multiple sources. First, the voltammetric peaks of different species often overlap when several ions coexist in solution, making it difficult to resolve the target ion with accuracy. Second, surface contamination or variations in the electrolyte composition can induce drift in the signal response curve, thereby reducing measurement stability. Third, electronic noise originating from instrumentation or environmental 

10 

> _J. Liu et al.                                                                                                                                                                                                                                       International Journal of Electrochemical Science 20 (2025) 101209_ 

## **Table 10** 

Performances of Functional Nucleic Acid-Modified Electrochemical Sensors. 

|Functional Nucleic Acid Modifcation|Detected Heavy Metal|Detection Methods|Detection|Linear Range|Sample Recoveries|References|
|---|---|---|---|---|---|---|
|Materials|Ions||Limits|(ng/L)|(%)||
||||(ng/L)||||
|FNA|Pb²⁺|DPASV|0.02|1.036–10360000|92–109.4|[123]|
|(DNAzyme)|||||||
|FNA|Pb²⁺|DPASV|0.041|0.621–1036000|89.7–110.5|[126]|
|(DNA Walker)|||||||
|FNA|Hg2+|SWASV|1.705|1003–1003000|98.3–105.2|[127]|
|(Y-shaped DNA Sequences)|||||||
|FNA|Hg2+|Chronoamperometry|2.006|2.006–5.015|98.6–102.2|[128]|
|(HRP-DNA-Au Bio-bar Codes)|||||||
|FNA|Pb²⁺, Hg²⁺|DPASV|2000 (Pb²⁺)|5000–1000000 (Pb²⁺)|96.1–104.3 (Pb²⁺)|[129]|
|(M-shaped DNA Complexes)|||500 (Hg²⁺)|1000–1000000|97.2–108.5 (Hg²⁺)||
|||||(Hg²⁺)|||
|FNA|Pb²⁺|EIS|78.736|103.6–207200|92–116.3|[130]|
|(Guanine-rich Y-shaped DNA|||||||
|Sequences)|||||||
|FNA|Hg2+|DPASV|5.8|10–4000|80.87–127.92|[131]|
|(Thymine-rich DNA Sequences)|||||||



## **Table 11** 

Performances of Enzyme-Modified Electrochemical Sensors. 

|Enzyme Modifcation Materials|Detected Heavy Metal Ions|Detection Methods|Detection Limits|Linear Range|Sample Recoveries|References|
|---|---|---|---|---|---|---|
||||(ng/L)|(ng/L)|(%)||
|Enzyme|Pb²⁺, Hg²⁺|EIS|3936.8 (Pb²⁺)|103600–455840 (Pb²⁺)|90–140 (Pb²⁺)|[134]|
|(Urease)|||3610.8 (Hg²⁺)|4012–160480 (Hg²⁺)|90–102.5 (Hg²⁺)||
|Enzyme|Pb²⁺|EIS|8.288|20.72–207.2|97–105|[135]|
|(Choline Oxidase)|||||||



fluctuations may obscure weak target signals, further compromising detection sensitivity. Conventional data processing typically relies on manual signal curve correction and voltammetric peak decomposition by operators. This approach is not only labor-intensive and timeconsuming but also introduces subjectivity, as the results are highly ’ dependent on the operator s expertise [136]. 

Machine learning (ML), which enables the automated identification of patterns from data to facilitate predictions or decision-making, offers a powerful, data-driven approach to overcome these limitations [137]. Specifically, ML algorithms can automatically extract features from complex electrochemical signals and establish robust mapping models between these signals and the corresponding heavy metal ion types and concentrations. This capability facilitates the highly accurate identification and quantification of heavy metal ions, as illustrated in Fig. 2 [138]. 

Feature extraction for electrochemical signals of heavy metal ions involves projecting multidimensional voltammetric signals into 2D or 


![](_temp_30dedc3c_convert__images/_temp_30dedc3c_convert_.pdf-0011-10.png)


**Fig. 2.** The Processes of ML Algorithms for Electrochemical Signals of Heavy Metal Ions. 

3D space. This projection aims to separate the signal clusters corresponding to different ions, providing an intuitive basis for qualitative analysis and facilitating the subsequent development of mapping models. Common ML algorithms employed for this feature extraction task include principal component analysis (PCA), independent component analysis (ICA), and convolutional neural networks (CNN) [139]. 

The PCA algorithm treats each feature within the high-dimensional voltammetric signal as a variable and projects these variables onto a new set of orthogonal axes (principal components). In the resulting projection, these new dimensions represent the directions of maximum variance in the original dataset, which often correspond to the distinct electrochemical responses of different heavy metal ions. As an unsupervised learning method, PCA enables the visual discrimination of different heavy metal ion types or concentrations by analyzing the spatial distribution of samples in the principal component space, thereby providing a basis for preliminary qualitative analysis [140]. The ICA algorithm operates on the assumption that a measured voltammetric signal is a linear mixture of statistically independent source signals, which represent the ideal voltammetric responses of individual heavy metal ions. The goal of ICA is to deconvolute the composite signal and recover these underlying source components. This makes ICA particularly suitable for handling complex systems where multiple heavy metal ions coexist and their voltammetric peaks overlap significantly, establishing it as a powerful tool for feature extraction in such challenging scenarios [141]. In contrast, CNN can automatically learn discriminative local features, such as rising edge, falling edge, and peak shapes, directly from raw voltammetric signals without requiring manual feature specification. CNN architectures exhibit translational invariance, making them robust to minor shifts of the voltammetric signal along the potential axis. By utilizing multiple convolutional layers, CNNs can hierarchically learn local features from highly complex signals and maintain performance even under significant baseline drift or substantial background interference, demonstrating remarkable robustness [142]. 

Table 12 provides a systematic comparison of the characteristics of the ML-based feature extraction algorithms discussed in this section. 

Establishing an accurate mathematical mapping model between 

11 

> _J. Liu et al.                                                                                                                                                                                                                                       International Journal of Electrochemical Science 20 (2025) 101209_ 

## **Table 12** 

Characteristics of Electrochemical Signal Feature Extraction ML Algorithms. 

|Electrochemical Signal|Characteristics|Limitations|
|---|---|---|
|Feature Extraction ML|||
|Algorithms|||
|PCA|No need to specify|Need to assume a linear|
||principal component|projection relationship;|
||labels;<br>Good visualization effect;<br>Simplifed data structure|The physical meaning of<br>the extracted features may<br>not be clear|
|ICA|The extracted features|The source signals are|
||have clear physical|required to be independent|
||meanings;|and linearly mixed;|
||It can handle complex|The order and amplitude of|
||systems with multiple|the separated source|
||coexisting ions and|signals may not be|
||severely overlapping|determined|
||voltammetric peaks||
|CNN|It is capable of<br>automatically extracting|Algorithms require a large<br>amount of annotated data;|
||signal features;<br>Highly strong robustness|Algorithm models are<br>complicated;|
|||Poor interpretability|



electrochemical signals and heavy metal ion concentration is fundamental for achieving precise quantitative analysis. The choice of ML algorithms for this mapping function significantly influences the prediction performance. The commonly used ML algorithms for constructing these mapping models can be categorized into several groups: linear models, such as partial least squares regression (PLSR) and support vector machines (SVM); tree-based ensemble algorithms, such as random forest (RF); and neural networks, including artificial neural networks (ANN) and convolutional neural networks (CNN). 

PLSR effectively addresses the issue of multicollinearity, which occurs when input features (e.g., current and potential values from a voltammetric curve) are highly correlated. This is achieved by projecting the original features onto a new set of uncorrelated latent variables that maximize the covariance with the target concentration. As the absolute mainstream algorithm in chemometrics, PLSR is particularly suitable for modeling electrochemical signal data [143]. SVM algorithms handle nonlinear regression by mapping the original feature data into a higher-dimensional space using kernel functions, where a linear regression model can be applied. This approach provides the flexibility to capture complex, nonlinear relationships between features and is robust even with moderately sized training datasets. The SVM algorithm often exhibits good performance when the amount of feature data used to train the algorithm is not particularly large. RF is an ensemble method that constructs a multitude of decision trees and aggregates their predictions, thereby mitigating the risk of overfitting inherent in individual trees [144]. A key advantage of RF is its ability to provide a ranking of feature importance, offering valuable insight into which electrochemical features most significantly influence the concentration prediction and enhancing the model’s interpretability [145]. ANN algorithms are 

universal function approximators capable of modeling highly complex, nonlinear relationships between raw electrochemical signals and heavy metal ion concentrations. A significant advantage of ANNs is their capacity for end-to-end learning; they can process the entire voltammetric curve as input and autonomously learn relevant feature representations without requiring manual feature selection [146]. CNN algorithms, as previously discussed, serve a dual purpose: they automatically extract local features from raw voltammetric signals and subsequently function as a powerful regression model, establishing a complex mapping from those features to heavy metal ion concentrations [147]. 

Additionally, Table 13 provides a systematic comparison of the characteristics of the mapping model ML algorithms discussed in this section. 

Recent progress in ML-assisted electrochemistry has enabled innovative approaches for heavy metal ion detection. Yao et al. [148] engineered a novel electrochemical sensing platform using a BiFeO₃/MXene nanocomposite. The material demonstrated exceptional properties for sensing applications, including high electrical conductivity (1.2 × 10⁴ S/m), a large surface area (325 m²/g), and superior Pb²⁺ adsorption capability. The developed sensor achieved remarkable detection performance, exhibiting an ultra-wide linear range from 0.0001 to 3000 μg/L and an exceptionally low LOD of 0.0001 μg/L for Pb²⁺. A key innovation was the implementation of an Orthogonal Experimental Design-Machine Learning (OED-ML) hybrid strategy, which reduced the number of required experiments by 78 % while achieving a prediction accuracy of 99.5 % and excellent recovery rates of 98.8–101.3 %. The platform successfully integrates high sensitivity, with a response time under 3 s, and excellent selectivity, maintaining a detection error below 15 % for Pb²⁺. This work marks a substantial advancement in environmental monitoring technology. 

Kailasam et al. [149] developed an electrochemical sensor based on an Ag₂O-BiOBr/Nafion nanocomposite. The composite formed a uniform heterostructure with an average particle size of 80 nm and facilitated efficient electron transfer, as indicated by an electron transfer number of 1.92, both of which contributed to its strong electrochemical activity. The sensor demonstrated excellent operational stability, with less than 5 % signal attenuation observed after 30 days of continuous operation. Using differential pulse voltammetry (DPV), the sensor produced highly linear responses (R² = 0.98) for the simultaneous detection of Ni²⁺ and Cu²⁺ across tested concentration gradients. The researchers further leveraged the stripping voltammetric signal data to construct heavy metal ion concentration prediction models using ANN, SVM, and RF algorithms. The respective prediction accuracies for heavy metal ion concentrations were 89.5 % for ANN, 88.1 % for SVM, and 55.3 % for RF. The superior performance of the ANN and SVM models highlights – their greater efficacy for electrochemical signal based prediction of heavy metal ions. This study demonstrates a robust and economical platform for water quality assessment by effectively integrating stripping voltammetry with ML. 

Sreerama et al. [150] developed an electrochemical sensor for the simultaneous detection of Cd²⁺, Pb²⁺, Cu²⁺, and Hg²⁺ in water samples 

**Table 13** 

Characteristics of Mapping Model ML Algorithms. 

|Mapping Model ML|Representative|Characteristics|Limitations|
|---|---|---|---|
|Algorithms|Algorithms|||
|Linear Model|PLSR, SVM|Strong interpretability; PLSR algorithm has strong resistance to|The SVM algorithm has weak ftting ability for feature data|
|Algorithms||multicollinearity;|with strong nonlinear relationships;|
|||SVM algorithm can handle nonlinear feature regression problems|And its predictive performance is highly dependent on the|
|Tree Ensemble<br>Algorithms|RF|and is suitable for small feature sample amounts<br>High prediction accuracy;<br>Strong resistance to overftting;<br>Able to handle non-linear feature data ftting problems;|type of kernel function and parameter settings<br>The effciency of the algorithm operation decreases as the<br>amount of feature data increases;<br>Moderate interpretability|
|Neural Network<br>Algorithms|ANN, CNN|Able to provide feature importances<br>Powerful non-linear feature data ftting ability;<br>Capable of automatically ftting feature data|Great demand for the quantity of feature data;<br>High cost of algorithm training and operation;|
||||Poor interpretability|



12 

_J. Liu et al.                                                                                                                                                                                                                                       International Journal of Electrochemical Science 20 (2025) 101209_ 

using a nanogold-modified carbon filament electrode. To enhance the identification of heavy metal ions, a CNN model was developed to extract the features from the obtained stripping voltammetric signals. The model architecture consisted of two one-dimensional convolutional (1D-CNN) layers for feature extraction, followed by an ANN layer for classification. This hybrid design enhances the model’s ability to generalize from the training data and mitigates overfitting. 

Tao et al. [151] developed a novel electrode based on tin-tantalum oxide-doped vertical graphene (STO-VG) for real-time monitoring of Cd²⁺. To quantify the detected Cd²⁺, SVM models were developed using both a Linear Kernel (LK-SVM) and a Radial Basis Function kernel (RBF-SVM). The prediction accuracy of these models was evaluated using the Residual Prediction Deviation (RPD) metric, where a larger RPD value corresponds to greater predictive reliability. The results demonstrated that the RBF-SVM model (RPD = 3.37) achieved significantly superior performance compared to the LK-SVM model (RPD = 0.71). 

Collectively, these advancements demonstrate the transformative impact of integrating ML with electrochemical sensors in advancing heavy metal ion detection. The synergistic combination of these fields has proven highly effective in augmenting key analytical metrics, including interference resistance, detection sensitivity, and quantification accuracy. This ML-assisted paradigm has thus established itself as a robust and reliable framework for advanced water quality monitoring. Future progress is anticipated to stem from the development of more sophisticated ML models, which are poised to unlock further enhancements in sensor performance. These next-generation systems are projected to achieve lower detection limits, broader detection ranges, and superior selectivity, even with highly complex environmental conditions. 

## **5. Conclusion** 

Contamination of aquatic systems by hazardous heavy metal ions poses a significant global environmental and public health challenge due to their high toxicity, bioaccumulation tendency, and environmental persistence. Electrochemical sensing platforms have emerged as valuable tools for monitoring these pollutants, offering significant advantages such as low LOD, rapid response times, cost-effectiveness, and strong potential for on-site deployment. This review systematically examines recent advancements in the development of electrochemical sensors for heavy metal ion detection. It provides a critical analysis of representative studies using inorganic, organic, and biomaterial-based modifications to enhance sensor performance. Critical evaluation indicates that sensors modified with inorganic nanomaterials offer distinct advantages, including facile fabrication, excellent operational stability, and enhanced charge transfer properties, which collectively make them highly suitable for heavy metal detection applications. Organic materialbased modifications leverage their tunable molecular structures and functional groups to enhance sensor selectivity and mitigate matrix interference in complex environmental samples. Biomaterial-modified sensors exploit inherent biological recognition mechanisms to achieve exceptional performance, including ultra-low LODs, high molecular specificity, and robust operation in interfering environments. This review also details the pivotal role of ML in advancing electrochemical detection, primarily through feature extraction and predictive modeling. Feature extraction algorithms, such as PCA, ICA, and CNN, automatically resolve discriminative features from complex voltammetric signals, effectively mitigating interference from peak overlap and baseline drift. Subsequently, predictive modeling algorithms, including PLSR, SVM, RF, and ANN/CNN, establish robust quantitative relationships between the extracted features and target concentrations, enabling high-precision, interference-resistant identification and quantification of heavy metals. The synergy between advanced materials and intelligent data processing provides a critical foundation for developing nextgeneration intelligent, reliable, and field-deployable sensors for heavy 

metal ion detection systems. 

Future advancements in electrochemical sensing for heavy metal monitoring should prioritize the development of advanced modification materials with synergistic properties to enhance detection performance and the establishment of intelligent calibration algorithms robust enough for complex aqueous environments. These efforts should strategically address several critical research gaps: (1) expanding detection capabilities to understudied but highly toxic and regulated ions, such as Ni²⁺, Cr⁶⁺, Co²⁺, and Sb³ ⁺. This can be achieved through the rational design of COF- and MOF-based sensing interfaces with precisely tailored binding affinities; (2) advancing multiplexed detection platforms that utilize orthogonal recognition elements (e.g., aptamer-MOF-polymer hybrid systems) to enable the simultaneous and accurate quantification of multiple pollutant ions in complex, real-world wastewater – matrices; (3) establishing a robust structure function mapping framework, supported by Density Functional Theory (DFT) calculations and machine learning modeling, to guide the rational design of hybrid materials with optimized charge transfer, selective ion binding, and enhanced environmental stability; and (4) promoting the miniaturization and integration of sensing technologies to develop flexible, wearable, and potentially self-powering devices. Such platforms would enable real-time, dynamic tracking of heavy metal exposure with high conformability and biocompatibility, providing critical data at both personal and environmental levels. 

This review synthesized the current progress in material design and machine learning, establishing a foundation for designing nextgeneration sensing platforms that combine cost-effective fabrication with superior interference resistance and intelligent data processing. 

## **CRediT authorship contribution statement** 

**Yuan Yin:** Methodology, Investigation, Data curation. **Jing Liu:** Writing – review & editing, Writing – original draft, Investigation, Data curation, Conceptualization. **Gang Liu:** Supervision, Project administration. 

## **Declaration of Competing Interest** 

The authors of manuscript entitled ‘ _Recent Progress of Electrochemical Sensors for Accurate Detection of Heavy Metal Ions in Water: A Comprehensive Review_ ’ declare that they have no known competing interests or personal relationships that could have appeared to influence the work reported in this manuscript. 

Additionally, this manuscript has not been published elsewhere and is not under consideration by another journal. 

## **Acknowledgements** 

This study was supported by the National Key Research and Development Program (file no. 2021YFB3801000), Innovative Research Groups of Hubei Province (file no. 2022CFA038), and General Program of the National Natural Science Foundation of China (file no. 32471994). 

## **Data Availability** 

No data was used for the research described in this manuscript. 

## **References** 

- [1] S. Kanwel, F. Gulzar, H. Alofaysan, S. Tanriverdiyev, H. Jing, Toxic metal pollution in freshwater ecosystems: a systematic review of assessment methods using environmental and statistical indices, Mar. Pollut. Bull. 218 (2025) 118028, https://doi.org/10.1016/j.marpolbul.2025.118028. 

- [2] B.J. Manegabe, T.A.M. Msagati, A. Adeyemi Ojutalayo, M.-M.K. Ntabugi, J. B. Dewar, K. De Bryun, Assessment of heavy metals pollution in vegetables grown on irrigated soil and their potential threat to human health and global food 

13 

_International Journal of Electrochemical Science 20 (2025) 101209_ 

security, HEHA 14 (2025) 100129, https://doi.org/10.1016/j. heha.2025.100129. 

- [3] P. Sahu, A.R. Patel, A. Pandey, M. Hait, G.K. Patra, Assessment of heavy metal ion toxicity in wastewater: a comprehensive review, Inorg. Chim. Acta 585 (2025) 122751, https://doi.org/10.1016/j.ica.2025.122751. 

- [4] W. Wei, C. Li, C. Ye, Z. Xie, Y. Wang, Y. Zheng, C. Ma, Evaluation of contamination characteristics and source apportionment of heavy metals in river sediments and their risk to human health: a case study in the heilongjiang basin, China, Results In. Eng. (2025) 107498, https://doi.org/10.1016/j. rineng.2025.107498. 

- [5] G. Feyisa, B. Mekassa, L.B. Merga, Human health risks of heavy metals contamination of a water-soil-vegetables farmland system in toke kutaye of west shewa, Ethiopia, Toxicol. Rep. 14 (2025) 102061, https://doi.org/10.1016/j. toxrep.2025.102061. 

- [6] P.K. Monika Mahajan, A. Gupta, B. Singh, P. Vaish, R. Singh, R.P. Kothari, Singh, A comprehensive study on aquatic chemistry, health risk and remediation techniques of cadmium in groundwater, Sci. Total. Environ. 818 (2022) 151784, https://doi.org/10.1016/j.scitotenv.2021.151784. 

- [7] A.A. Saghir, F. Asmelash, M. Maryo, A. Boularbah, F. Kebede, Extent of natural soil cadmium, its bioavailability, and pollution treat analysis in the agroforestry systems of the gedeo zone of Southern Ethiopia, Heliyon 11 (2025) e42742, https://doi.org/10.1016/j.heliyon.2025.e42742. 

- [8] H. Li, Z. Yang, W. Zheng, L. Leng, J. Yang, W. Qu, H. Li, A review on monolithic remediators for Mercury pollution control in industrial flue gas and effluents, Sep. Purif. Technol. 363 (2025) 131917, https://doi.org/10.1016/j. seppur.2025.131917. 

- [9] Z. Ullah, Z. Chen, M.V. Ullah, M.I. Esteller, M.A. Khan, J. Hussain, Iqbal, Groundwater vulnerability to arsenic in semi-arid region of Pakistan: sources identification, spatial analysis, and public health risks evaluation, Desalin. Water Treat. (2025) 101481, https://doi.org/10.1016/j.dwt.2025.101481. 

- [10] L.D. Abo, H.A. Areti, M. Jayakumar, M. Rangaraju, S. Subashini, Nanobiomaterials-enabled sensors for heavy metal detection and remediation in wastewater systems: advances in synthesis, characterization, and environmental applications, Results In. Eng. 27 (2025) 105694, https://doi.org/10.1016/j. rineng.2025.105694. 

- [11] K. Miao, S. Chen, J. Zhou, The X-ray absorption spectroscopy for advanced battery systems, Sustain. Mater. Technol. 45 (2025) e01608, https://doi.org/ 10.1016/j.susmat.2025.e01608. 

- [12] M. Jiang, C. Zhang, Y. Chen, M. Sun, R. Liu, Y. Lv, Inductively coupled plasma mass spectrometry-based immunoassay: an update from 2015 to 2025, TracTrend Anal. Chem. 191 (2025) 118317, https://doi.org/10.1016/j.trac.2025.118317. 

- [13] E. Nanou, N. Pliatsika, D. Stefas, D. Polygenis, S. Couris, Laser induced breakdown spectroscopy as an emerging technique for olive oil, milk and honey authentication and traceability: a review, J. Food Compos. Anal. 144 (2025) 107650, https://doi.org/10.1016/j.jfca.2025.107650. 

- [14] S. Bodur, B.K. Tutar, S.E. Bodur, O.F. Tutar, S. Bakırdere, A new analytical[¨] protocol for the determination of cadmium in sunflower oil samples: Micro–sampling cold vapor generation–atomic absorption spectrometry after spraying based microextraction method, Food Chem. 487 (2025) 144738, https://doi.org/10.1016/j.foodchem.2025.144738. 

- [15] R.P. Kalambate, P.K. Kalambate, W. Laiwattanapaisal, Revolutionizing melamine detection: Cutting-edge advances from traditional analyses to state-of-the-art electrochemical sensors, Next Mater. 3 (2024) 100085, https://doi.org/10.1016/ j.nxmate.2023.100085. 

- [16] Z. Zhang, N. Zare, T. Wu, M. Ghalkhani, Y. Wen, N. Zhong, H. Karimi-Maleh, What happens in toxic metal detection using an electrochemical aptasensor? A review, Inorg. Chem. Commun. 178 (2025) 114459, https://doi.org/10.1016/j. inoche.2025.114459. 

- [17] X. Li, Y. Ni, C. Liu, S. Xu, W. Shu, H. Liang, M. Chen, An electrochemical sensor based on immobilized cystathionine β-synthase (CBS) enzymes and pd@cuo modified covalent organic framework for specific detection of homocysteine, Microchem. J. 214 (2025) 113950, https://doi.org/10.1016/j. microc.2025.113950. 

- [18] X. Li, Q. Wang, C.-R. Qin, A.-L. Liu, Y. Chen, Enhanced electrochemical immunosensor utilizing pATA/AuNPs for sensitive detection of the leukemiaassociated biomarker CD123 in bone marrow supernatant, Eur. J. Pharm. Sci. 211 (2025) 107124, https://doi.org/10.1016/j.ejps.2025.107124. 

- [19] Y. Tian, J. Liu, J. Qiao, F. Ge, Y. Yang, Q. Zhang, Advancements in electrochemical sensing technology for heavy metal ions detection, Food Chem. X. 25 (2025) 102204, https://doi.org/10.1016/j.fochx.2025.102204. 

- [20] G. Levanen, F. Razan, S. Bretin, S. Betelu, K. Michel, F. Geneste, Electrochemical detection of lead, cadmium, and Mercury with selective preconcentration on ligand-modified electrodes, Electroanal. Chem. 991 (2025) 119189, https://doi. org/10.1016/j.jelechem.2025.119189. 

- [21] B. Li, X. Xie, T. Meng, X. Guo, Q. Li, Y. Yang, H. Jin, C. Jin, X. Meng, H. Pang, Recent advance of nanomaterials modified electrochemical sensors in the detection of heavy metal ions in food and water, Food Chem. 440 (2024) 138213, https://doi.org/10.1016/j.foodchem.2023.138213. 

- [22] M. Dali, K. Zinoubi, A. Chrouda, S. Abderrahmane, S. Cherrad, N. JaffrezicRenault, A biosensor based on fungal soil biomass for electrochemical detection of lead (II) and cadmium (II) by differential pulse anodic stripping voltammetry, Electroanal. Chem. 813 (2018) 9–19, https://doi.org/10.1016/j. jelechem.2018.02.009. 

- [23] G. Herzog, V. Beni, Stripping voltammetry at micro-interface arrays: a review, Anal. Chim. Acta 769 (2013) 10–21, https://doi.org/10.1016/j.aca.2012.12.031. 

- [24] H. Abd El-Raheem, R. Helim, R.Y.A. Hassan, A.F.A. Youssef, H. Korri-Youssoufi, C. Kraiya, Electrochemical methods for the detection of heavy metal ions: from sensors to biosensors, Microchem. J. 207 (2024) 112086, https://doi.org/ 10.1016/j.microc.2024.112086. 

- [25] C. Kokkinos, A. Economou, Emerging trends in biosensing using stripping voltammetric detection of metal-containing nanolabels - a review, Anal. Chim. Acta 961 (2017) 12–32, https://doi.org/10.1016/j.aca.2017.01.016. 

- [26] Y. Jin, D. Tong, W. Zhang, J. Wu, D. Ma, Y. Tai, C. Cui, X. Li, L. Yang, G. Xu, Water-phase induced synthesis of ZnCo/N-PC synergized with NACS for the electrochemical rapid determination of heavy metal ions in water and grains, Microchem. J. 217 (2025) 114971, https://doi.org/10.1016/j. microc.2025.114971. 

- [27] A. Rubino, R. Queiros, Electrochemical determination of heavy metal ions ´ applying screen-printed electrodes based sensors. A review on water and environmental samples analysis, Talanta Open 7 (2023) 100203, https://doi.org/ 10.1016/j.talo.2023.100203. 

- [28] J. Jjagwe, P.W. Olupot, R. Kulabako, S. Electrochemical sensors modified with iron oxide nanoparticles/ nanocomposites for voltammetric detection of pb (II) in water: a review, Heliyon 10 (2024) e29743, https://doi.org/10.1016/j. heliyon.2024.e29743. 

- [29] N. Esfandiari, M. Aliofkhazraei, Advances in the determination of trace amounts of iron cations through electrochemical methods: a comprehensive review of principles and their limits of detection, Talanta 277 (2024) 126365, https://doi. org/10.1016/j.talanta.2024.126365. 

- [30] S.D. Illesinghe, V. Sundaresan, Electrochemical detection of heavy metal ions adsorbed on microplastics with varying surface charges, Sens. And. Actuators Rep. 8 (2024) 100241, https://doi.org/10.1016/j.snr.2024.100241. 

- [31] X. Tang, H. Han, L. Li, H. Wang, Electrodes functionalized with advanced recognition materials for trace electrochemical sensing of uranyl ion, Microchem. J. 199 (2024) 109924, https://doi.org/10.1016/j.microc.2024.109924. 

- [32] Y. Tang, Q. Zhang, H. Yuan, X. Wang, L. Xu, G. Wang, M. Zhang, P. Lu, H. Zhong, Y. Wang, Recent applications and challenges of inorganic nanomaterial-based biosensing devices for detecting nucleic acid biomarkers, Adv. Sens. And. Energy Mater. 4 (2025) 100136, https://doi.org/10.1016/j.asems.2025.100136. 

- [33] F. Yuan, Y. Xia, Q. Lu, Q. Xu, Y. Shu, X. Hu, Recent advances in inorganic functional nanomaterials based flexible electrochemical sensors, Talanta 244 (2022) 123419, https://doi.org/10.1016/j.talanta.2022.123419. 

- [34] Y. GadelHak, S.H.M. Hafez, H.F.M. Mohamed, E.E. Abdel-Hady, R. Mahmoud, Nanomaterials-modified disposable electrodes and portable electrochemical systems for heavy metals detection in wastewater streams: a review, Microchem. J. 193 (2023) 109043, https://doi.org/10.1016/j.microc.2023.109043. 

- [35] D. Kothari, A. Kumar, Metallic, carbon-based, and polymeric nanomaterials: transforming dairy farming practices for sustainability, Food Chem. X. 29 (2025) 102640, https://doi.org/10.1016/j.fochx.2025.102640. 

- [36] S. Zhang, W. Zhao, J. Zeng, Z. He, X. Wang, Z. Zhu, R. Hu, C. Liu, Q. Wang, Wearable non-invasive glucose sensors based on metallic nanomaterials, Mater. Today Biol. 20 (2023) 100638, https://doi.org/10.1016/j.mtbio.2023.100638. 

- [37] M. Wang, X. Zheng, B.T. Oba, Y. Lin, C. Shen, X. Huang, F. Yang, Q. Xiao, Y. Ding, Innovations in nanomaterials for remediation of heavy metal− polluted soil: advances, mechanistic insights, and future prospects, Nano Mater. Sci. (2025) S2589965125000686, https://doi.org/10.1016/j.nanoms.2025.06.008. 

- [38] G. Zhao, X. Wang, G. Liu, Y. Cao, N. Liu, N. Thi Dieu Thuy, L. Zhang, M. Yu, A flexible and disposable electrochemical sensor for the evaluation of arsenic levels: a new and efficient method for the batch fabrication of chemically modified electrodes, Anal. Chim. Acta 1194 (2022) 339413, https://doi.org/ 10.1016/j.aca.2021.339413. 

- [39] J. Chen, Z. Zhang, J. Zhou, T. Zeng, H. Xiao, T. Yang, T. Xu, L. Wang, W. Wang, Pyridine-assisted electrodeposition of Au(1 1 1)-dominant gold nanonetworks on glassy carbon electrode for anodic stripping voltammetry analysis of As(III), Se (IV) and Cu(II), Microchem. J. 200 (2024) 110311, https://doi.org/10.1016/j. microc.2024.110311. 

- [40] C.T. Thanh, N.T. Huyen, V.T. Thu, P.V. Trinh, N.V. Tu, B.H. Thang, T.V. Hau, D. Tuan, M.T. Phuong, P.T. Binh, P.N. Minh, H. Abe, N.V. Chuc, Improved electrochemical sensor based on 3D porous Gra-DCNTs-AuNPs-PANi hybrid film for fenitrothion detection, Mater. Lett. 386 (2025) 138209, https://doi.org/ 10.1016/j.matlet.2025.138209. 

- [41] Y. Chen, Y. Liu, P. Zhao, Y. Liang, Y. Ma, H. Liu, J. Hou, C. Hou, D. Huo, Sulfhydryl-functionalized 3D MXene-AuNPs enabled electrochemical sensors for the selective determination of Pb[2][+] , Cu[2][+] , and Hg[2][+] in grain, Food Chem. 446 (2024) 138770, https://doi.org/10.1016/j.foodchem.2024.138770. 

- [42] K. Karn-orachai, R. Niamlaoong, A. Ngamaroonchote, P. Wattanasin, AuNPsSPCE: a versatile sensor for multi-heavy metal detection in water, Microchem. J. 210 (2025) 113028, https://doi.org/10.1016/j.microc.2025.113028. 

- [43] S. Chen, H. Li, R. He, L. Feng, C. Lv, S. Zhang, X. Zhao, G. Zhao, Sensitive electrochemical detection of As(III) in soil based on CoFe2O4/ AuNPs/IL nanocomposite modified electrode: insight into the sensing mechanism of a dual electrocatalysis system, Microchem. J. 203 (2024) 110849, https://doi.org/ 10.1016/j.microc.2024.110849. 

- [44] S. Wu, Y. Liang, H. Guo, An electrochemical sensor for sub-attomolar determination of aluminum ion with an ultra-wide response range, Microchem. J. 195 (2023) 109527, https://doi.org/10.1016/j.microc.2023.109527. 

- [45] N.H. Ramli, N. Mohamad Nor, A.H. Abu Bakar, N.D. Zakaria, Z. Lockman, K. Abdul Razak, Platinum-based nanoparticles: a review of synthesis methods, surface functionalization, and their applications, Microchem. J. 200 (2024) 110280, https://doi.org/10.1016/j.microc.2024.110280. 

14 

_International Journal of Electrochemical Science 20 (2025) 101209_ 

- [46] X. Lin, Z. Zhu, C. Zhao, S. Li, Q. Liu, A. Liu, L. Lin, X. Lin, Robust oxidase mimicking activity of protamine-stabilized platinum nanoparticles units and applied for colorimetric sensor of trypsin and inhibitor, Sens. Actuator BChem. 284 (2019) 346–353, https://doi.org/10.1016/j.snb.2018.12.109. 

- [47] C. Pechyen, B. Tangnorawich, S. Toommee, R. Marks, Y. Parcharoen, Green synthesis of metal nanoparticles, characterization, and biosensing applications, Sens. Int. 5 (2024) 100287, https://doi.org/10.1016/j.sintl.2024.100287. 

- [48] J. Ru, X. Wang, J. Zhao, J. Yang, Z. Zhou, X. Du, X. Lu, Evaluation and development of GO/UiO-67@PtNPs nanohybrid-based electrochemical sensor for invisible arsenic (III) in water samples, Microchem. J. 181 (2022) 107765, https://doi.org/10.1016/j.microc.2022.107765. 

- [49] M.B. Elamin, A. Chrouda, S.M.A. Ali, L.M. Alhaidari, M. Jabli, R.M. Alrouqi, N. J. Renault, Electrochemical sensor based on gum arabic nanoparticles for rapid and in-situ detection of different heavy metals in real samples, Heliyon 10 (2024) e26364, https://doi.org/10.1016/j.heliyon.2024.e26364. 

- [50] J. Ru, X. Wang, Z. Zhou, J. Zhao, J. Yang, X. Du, X. Lu, Fabrication of octahedral GO/UiO-67@PtNPs nanocomposites as an electrochemical sensor for ultrasensitive recognition of arsenic (III) in Chinese herbal Medicine, Anal. Chim. Acta 1195 (2022) 339451, https://doi.org/10.1016/j.aca.2022.339451. 

- [51] M. Jayaprakash, S. Kannappan, An overview of a sustainable approach to the biosynthesis of AgNPs for electrochemical sensors, Arab. J. Chem. 15 (2022) 104324, https://doi.org/10.1016/j.arabjc.2022.104324. 

- [52] A. Dhaffouli, Eco-friendly nanomaterials synthesized greenly for electrochemical sensors and biosensors, Microchem. J. 217 (2025) 115051, https://doi.org/ 10.1016/j.microc.2025.115051. 

- [53] Y. Yulirohyami, I. Fatimah, D. Siswanta, M. Mudasir, Green synthesis of AgNPsdithizone@chitosan for highly selective and reusable electrochemical sensors of Hg2+, Microchem. J. 214 (2024) 114015 https://doi.org/10.1016/j. microc.2025.114015. 

- [54] B. Ajdari, T. Madrakian, A. Afkhami, Development of an electrochemical sensor utilizing MWCNs-poly (2-aminothiophenol) @AgNPs nanocomposite for the simultaneous determination of Pb[2][+] and Cd[2][+] in food samples, Food Chem. 477 (2025) 143529, https://doi.org/10.1016/j.foodchem.2025.143529. 

- [55] P. Dutta, G. Gupta, A mini review on wearable electronics in breathomics: the use of metal oxide nanomaterials, Microchem. J. 214 (2025) 113911, https://doi. org/10.1016/j.microc.2025.113911. 

- [56] L.V. Hublikar, S.V. Ganachari, F.A. Shilar, N. Raghavendra, Recent advances in transition metal oxide nanomaterials for solar cell applications: a status review and technology perspectives, Mater. Res. Bull. 187 (2025) 113351, https://doi. org/10.1016/j.materresbull.2025.113351. 

- [57] C.V.V.M. Gopi, S. Alzahmi, M.Y. Al-Haik, Y.A. Kumar, F. Hamed, Y. Haik, I. M. Obaidat, Recent advances in pseudocapacitive electrode materials for high energy density aqueous supercapacitors: combining transition metal oxides with carbon nanomaterials, Mater. Today Sustain 28 (2024) 100981, https://doi.org/ 10.1016/j.mtsust.2024.100981. 

- [58] A. Lochab, K. Jindal, A. Chowdhuri, M. Tomar, R. Saxena, Metal oxide based carbon nanocomposite as sensing platform for electrochemical detection of cadmium- computational and experimental approach, Microchem. J. 198 (2024) 110125, https://doi.org/10.1016/j.microc.2024.110125. 

- [59] H. Xu, Q.-Y. Wang, M. Jiang, S.-S. Li, Application of valence-variable transitionmetal-oxide-based nanomaterials in electrochemical analysis: a review, Anal. Chim. Acta 1295 (2024) 342270, https://doi.org/10.1016/j.aca.2024.342270. 

- [60] J. An, M. Luo, M. Li, H. Cui, Y. Liu, Development of an advanced electrochemical biosensor for choline detection using MXene, MWCNT-AuNPs, and Fe3O4NPs, Microchem. J. 214 (2025) 114034, https://doi.org/10.1016/j. microc.2025.114034. 

- [61] A.S. Pittman, Y. Cao, D.K. Sam, Z.-M. Tao, H. Li, Synergistic utilization of carbonintegrated covalent organic frameworks and magnetic Fe₃O₄ nanoparticles for efficient recovery of gold and copper from E-waste, Chem. Eng. J. 521 (2025) 166987, https://doi.org/10.1016/j.cej.2025.166987. 

- [62] M. Zhang, W. Guo, A facile electrochemical sensor based on amino-functionalized magnetic nanoparticles for simultaneous detection of lead and mercuric ions, J. Food Compos. Anal. 119 (2023) 105232, https://doi.org/10.1016/j. jfca.2023.105232. 

- [63] D. Singh, S. Shaktawat, S.K. Yadav, R. Verma, K.R. Singh, J. Singh, Chitosanassisted self-assembly of flower-shaped ε-Fe2O3 nanoparticles on screen-printed carbon electrode for impedimetric detection of Cd[2][+] , Pb[2][+] , and Hg[2][+] heavy metal ions in various water samples, Int. J. Biol. Macromol. 265 (2024) 130867, https://doi.org/10.1016/j.ijbiomac.2024.130867. 

- [64] K. Doloi, N. Badhai, D. Mohanta, Nanoscale Ag2O decorated UiO-66 metal organic framework for simultaneous electrochemical sensing of heavy metals, Cd2+ and Hg2+, Mater. Res. Bull. 170 (2024) 112558 https://doi.org/10.1016/j. materresbull.2023.112558. 

- [65] F. Liu, Y. Zhang, W. Yin, C. Hou, D. Huo, B. He, L. Qian, H. Fa, Sensor. A high–selectivity electrochemical sensor for ultra-trace lead (II) detection based on a nanocomposite consisting of nitrogen-doped graphene/gold nanoparticles functionalized with ETBD and Fe3O4@TiO2 core–shell nanoparticles, Actuator BChem. 242 (2017) 889–896, https://doi.org/10.1016/j.snb.2016.09.167. 

- [66] C. Mabrouk, J. Wannassi, P.A. Salazar-Carballo, S. Carinelli, A.J. Gross, H. Kahri, N. Jaffrezic-Renault, H. Barhoumi, ZnO nanoparticles coated with EDTA and ag nanoparticles (ZnO@EDTA-Ag NPs) for enhanced electrochemical detection of Cu2+ ions in food and environmental samples, Microchem. J. 212 (2025) 113562, https://doi.org/10.1016/j.microc.2025.113562. 

- [67] I. Mustafa, B. Basha, S. Zulfiqar, A. Tahir, F. Hanif, M.S. Al-Buriahi, M. Akhtar, K. Chaudhary, Mater. Chem. Phys. 305 (2023) 127991, https://doi.org/10.1016/ j.matchemphys.2023.127991. 

- [68] S. Moussaoui, F. Smaili, S.E. Berrabah, Fabrication of novel electrochemical sensor based on NiO-nanoparticles for copper detection in drinking water, Inorg. Chem. Commun. 158 (2023) 111563, https://doi.org/10.1016/j. inoche.2023.111563. 

- [69] E.M. Maldaye, I.O. Oladele, B.O. Adewuyi, E.T. Fisha, Eco-friendly synthesis of silica and carbon-based nanoparticles from natural resources: a sustainable approach, Next Res. 2 (2025) 100893, https://doi.org/10.1016/j. nexres.2025.100893. 

- [70] M. Singh, I. Malik, F. Hazzazi, A. Kumar, Advances in carbon-dots based nanomaterials for electrocatalytic water splitting: fundamental, challenges, and future prospects, Int. J. Hydrog. Energy 179 (2025) 151623, https://doi.org/ 10.1016/j.ijhydene.2025.151623. 

- [71] S. Mahapatra, D.S. Dkhar, A. Singh, P. Chandra, Metallic nanoparticle-based glassy carbon electrodes for smart biosensing, Curr. Opin. Electro 54 (2025) 101748, https://doi.org/10.1016/j.coelec.2025.101748. 

- [72] A. Cantalapiedra, M.J. Gismera, J.R. Procopio, M.T. Sevilla, Electrochemical sensor based on polystyrene sulfonate–carbon nanopowders composite for cu (II) determination, Talanta 139 (2015) 111–116, https://doi.org/10.1016/j. talanta.2015.02.049. 

- [73] D. Chu, C. Gao, Z. Ji, Y. Li, Q. Jin, Y. He, W. Bai, Advancements in CNT research: integrating machine learning with microscopic simulations, macroscopic techniques, and application of performance prediction and functional optimization, Mater. Today Chem. 45 (2025) 102616, https://doi.org/10.1016/j. mtchem.2025.102616. 

- [74] S. Awasthi, A. Srivastava, D. Kumar, S.K. Pandey, N.M. Mubarak, M.H. Dehghani, K. Ansari, An insight into the toxicological impacts of carbon nanotubes (CNTs) on human health: a review, Environ. Adv. 18 (2024) 100601, https://doi.org/ 10.1016/j.envadv.2024.100601. 

- [75] S. Yücer, B. Sarac, F. Ciftci, Electrochemical biosensors based on carbon nanotubes (CNTs) used to diagnosis pancreatic and liver cancer, Microchem. J. 215 (2025) 114289, https://doi.org/10.1016/j.microc.2025.114289. 

- [76] J. Wei, L. Wang, J. Hu, W. Wei, Y. Yang, Y. Song, Y. Li, G. Gao, Development of an origami paper-based electrochemical sensor using N-doped graphene for simultaneous detection of Cd(II), Pb(II), and Hg(II) in water, Microchem. J. 212 (2025) 113223, https://doi.org/10.1016/j.microc.2025.113223. 

- [77] Z. Lu, H. Zhang, M. Toivakka, C. Xu, Current progress in functionalization of cellulose nanofibers (CNFs) for active food packaging, Int. J. Biol. Macromol. 267 (2024) 131490, https://doi.org/10.1016/j.ijbiomac.2024.131490. 

- [78] J. Lin, K. Karuppasamy, R. Bose, D. Vikraman, S. Alameri, T. Maiyalagan, H.S. Kim, A. Alfantazi, J.G. Korvink, B. Sharma, Research trends in electrospun conducting polymers derived CNFs and their composite as the potential electrodes for high-performance flexible supercapacitors, J. Energy Storage 96 (2024) 112605, https://doi.org/10.1016/j.est.2024.112605. 

- [79] B. Zhang, J. Chen, H. Zhu, T. Yang, M. Zou, M. Zhang, M. Du, Facile and Green fabrication of size-controlled AuNPs/CNFs hybrids for the highly sensitive simultaneous detection of heavy metal ions, Electrochim. Acta 196 (2016) 422–430, https://doi.org/10.1016/j.electacta.2016.02.163. 

- [80] J. Li, C. Wang, W. Shi, J. Wu, S. Si, W. Qi, Y. Liu, J. Zhao, X. Kang, S. Niu, H. Li, K. Liu, L. Wang, Graphene oxide for selective uranium extraction from seawater and wastewater: from graphene oxide powder to its assembly of macroscopic materials, Sustain. Mater. Technol. 45 (2025) e01462, https://doi.org/10.1016/j. susmat.2025.e01462. 

- [81] G. Verma, R. Goel, N. Kaur, M.K. Singh, S.M. Rangappa, S. Siengchin, Understanding behaviour of graphene in natural fibre composites: a comprehensive review, Eur. Polym. J. 232 (2025) 113959, https://doi.org/ 10.1016/j.eurpolymj.2025.113959. 

- [82] H. Nikpourian, A. Allahbakhsh, Mechanisms involved in solar steam generation via graphene-based photothermal active materials, Chem. Eng. J. 512 (2025) 162457, https://doi.org/10.1016/j.cej.2025.162457. 

- [83] S. Sharma, M. Bhende, P. Mulwani, S. Patil, A comprehensive exploration of graphene and graphene oxide based hydrogels - methods, characteristics, and applications, J. Indian. Chem. 102 (2025) 101782, https://doi.org/10.1016/j. jics.2025.101782. 

- [84] X. Yuan, X. Wu, Y. Ling, S. Li, J. Chen, Z. Zhang, In situ bismuth ion exchange plating micro-electrochemical sensor based on laser-induced graphene for trace Cd2+ and Pb2+ detection, J. Environ. Chem. Eng. 12 (2024) 112161, https://doi. org/10.1016/j.jece.2024.112161. 

- [85] Y. Chen, P. Zhao, Y. Liang, Y. Ma, Y. Liu, J. Zhao, J. Hou, C. Hou, D. Huo, A sensitive electrochemical sensor based on 3D porous melamine-doped rGO/ MXene composite aerogel for the detection of heavy metal ions in the environment, Talanta 256 (2023) 124294, https://doi.org/10.1016/j. talanta.2023.124294. 

- [86] M. Mahadik, G.A. Bodkhe, N. Ingle, H. Patil, M. Shirsat, Selective and sensitive detection of pb (II) from aqueous solutions at optimized ph and analyzed for repeatability and reproducibility, Appl. Phys. A. 131 (2025) 125, https://doi.org/ 10.1007/s00339-024-08235-7. 

- [87] Y. Hu, X. Wang, W. Li, Y. Lai, Y. Chen, Z. Wei, H. Yang, Metal-organic frameworks and related materials for nonenzymatic electrochemical glucose sensors, Int. J. Electrochem. Sc. 19 (2024) 100466, https://doi.org/10.1016/j. ijoes.2024.100466. 

- [88] M. Yin, L. Zhang, X. Wei, J. Sun, D. Xu, Detection of antibiotics by electrochemical sensors based on metal-organic frameworks and their derived materials, Microchem. J. 183 (2022) 107946, https://doi.org/10.1016/j. microc.2022.107946. 

- [89] A. Lochab, M. Saxena, K. Jindal, M. Tomar, V. Gupta, R. Saxena, Thiolfunctionalized multiwall carbon nanotubes for electrochemical sensing of 

15 

> _J. Liu et al.                                                                                                                                                                                                                                       International Journal of Electrochemical Science 20 (2025) 101209_ 

thallium, Mater. Chem. Phys. 259 (2021) 124068, https://doi.org/10.1016/j. matchemphys.2020.124068. 

- [90] M. Li, J. Wu, L. Cui, H. Ju, Selective and sensitive electrochemical determination of pb 2+ based on highly adsorptive WO x –ethylenediamine nanowires, Electroanal. Chem. 757 (2015) 23–28, https://doi.org/10.1016/j. jelechem.2015.09.001. 

- [91] J. Gayathri, S. Sivalingam, S.S. Narayanan, Synthesis and characterization of schiff base ligand-mutliwalled carbon nanotubes as Mercury-free electrochemical sensor for detecting toxic metals in aquatic treatment, Diam. Relat. Mater. 136 (2023) 109984, https://doi.org/10.1016/j.diamond.2023.109984. 

- [92] L. Ma, W.-Y. Pei, J. Yang, J.-F. Ma, A new thiacalix[4]arene-based metal-organic framework as an efficient electrochemical sensor for trace detection of Cd2+ and Pb2+, Food Chem. 441 (2024) 138352 https://doi.org/10.1016/j. foodchem.2023.138352. 

- [93] A. Dube, S.J. Malode, A.N. Alodhayb, K. Mondal, N.P. Shetti, Conducting polymer-based electrochemical sensors: progress, challenges, and future perspectives, Talanta Open 11 (2025) 100395, https://doi.org/10.1016/j. talo.2024.100395. 

- [94] H.A. El-Raheem, A.S. Alawam, H.A. Rudayni, A.A. Allam, R. Helim, R. Mahmoud, N.I. Wardani, W. Alahmad, Eco-friendly features in molecularly imprinted polymers for applications in electrochemical and optical sensing, Microchem. J. 212 (2025) 113443, https://doi.org/10.1016/j.microc.2025.113443. 

- [95] B. Ajdari, T. Madrakian, A. Afkhami, Development of an electrochemical sensor utilizing MWCNs-poly(2-aminothiophenol) @AgNPs nanocomposite for the simultaneous determination of Pb2+ and Cd2+ in food samples, Food Chem. 477 (2025) 143529, https://doi.org/10.1016/j.foodchem.2025.143529. 

- [96] M. Maheshwaran, K.K.S. Kumar, A highly sensitive electrochemical detection of multiple heavy metal ions in water using PAni–RYFG/GCE modified electrode: experimental and DFT studies, Microchem. J. 213 (2025) 113654, https://doi. org/10.1016/j.microc.2025.113654. 

- [97] M. Maheshwaran, G. Sivaraman, K.K.S. Kumar, An electrochemical voltammetric response of Hg2+ and Pb2+ ions using polyaniline-benzothiazole composite modified GCE electrode: synthesis, characterization and quantum chemical calculation, Microchem. J. 197 (2024) 109865, https://doi.org/10.1016/j. microc.2023.109865. 

- [98] Y. Wu, X. Gao, Y. Li, Electrochemical sensors based on polyaniline nanocomposites for detecting Cd(II) in wastewater, Int. J. Electrochem. Sc. 19 (2024) 100519, https://doi.org/10.1016/j.ijoes.2024.100519. 

- [99] L. Zhang, Y. Zhang, W.-T. Chen, X. An, H. Liu, F. Chang, S. Gao, G. Hu, Recent advances and perspectives in functionalized nanocomposites for electrochemical sensing of toxic environmental heavy metal ions, Coord. Chem. Rev. 542 (2025) 216859, https://doi.org/10.1016/j.ccr.2025.216859. 

- [100] P. Chen, H. Wang, H. Li, B. Niu, H. Guo, Z. Chen, A high-activity Fe-based MOFs fabricated through ultrasound strategy for electrochemical sensor of heavy metal ions and dopamine, Electroanal. Chem. 957 (2024) 118129, https://doi.org/ 10.1016/j.jelechem.2024.118129. 

- [101] H. Sun, H. Liu, M. Fang, Z. Chen, Y. Zhang, X. Tan, Electrochemical sensor of cu nanoparticles on cu based metal organic frame works hybridized indium tin oxides glasses for Pb2+ detection, J. Environ. Chem. Eng. 12 (2024) 112069, https://doi.org/10.1016/j.jece.2024.112069. 

- [102] Y. Zhang, Y. Xu, N. Li, X. Liu, Y. Ma, Siyi Yang, H. Luo, C. Hou, D. Huo, An ultrasensitive electrochemical sensor based on antimonene simultaneously detect multiple heavy metal ions in food samples, Food Chem. 421 (2023) 136131, https://doi.org/10.1016/j.foodchem.2023.136131. 

- [103] H. Liu, H. Sun, M. Fang, Y. Zhang, M. Kong, Z. Lv, X. Tan, Detection of Pb(II) in water via a NH2-MIL-53(Fe)@ITO electrochemical sensor, Mater. Chem. Phys. 314 (2024) 128833, https://doi.org/10.1016/j.matchemphys.2023.128833. 

- [104] P. Xiao, G. Zhu, X. Shang, B. Hu, B. Zhang, Z. Tang, J. Yang, J. Liu, An Fe-MOF/ MXene-based ultra-sensitive electrochemical sensor for arsenic(III) measurement, Electroanal. Chem. 916 (2022) 116382, https://doi.org/10.1016/j. jelechem.2022.116382. 

- [105] Y. Zhang, Y. Xu, Y. Ma, H. Luo, J. Hou, C. Hou, D. Huo, Ultra-sensitive electrochemical sensors through self-assembled MOF composites for the simultaneous detection of multiple heavy metal ions in food samples, Anal. Chim. Acta 1289 (2024) 342155, https://doi.org/10.1016/j.aca.2023.342155. 

- [106] Y. Zhang, S. Jin, R. Liu, Z. Liu, L. Gong, L. Zhang, T. Zhao, W. Yin, S. Chen, H. Fa, L. Niu, A portable magnetic electrochemical sensor for highly efficient Pb(II) detection based on bimetal composites from Fe-on-Co-MOF, Environ. Res. 250 (2024) 118499, https://doi.org/10.1016/j.envres.2024.118499. 

- [107] J. Liu, W. Wang, D. Xu, Y. Duan, Z. Chen, S. Liu, G. Qin, J. Shi, Y. Tan, S. Yang, L. Li, 2D boat-sheet-like co (II) metal organic frameworks enabled functionalized electrochemical sensing interface with enrichment capabilities for Mercury ion detection in urine sample, Microchem. J. 212 (2025) 113547, https://doi.org/ 10.1016/j.microc.2025.113547. 

- [108] Q. Liang, W. Xiao, C. Zhang, D. Zhu, S.-L. Wang, S.-Y.U. Tian, T. Long, E.-L. Yue, J.-J. Wang, X.-Y. Hou, MOFs-based Fe@YAU-101/GCE electrochemical sensor platform for highly selective detecting trace multiplex heavy metal ions, Talanta 259 (2023) 124491, https://doi.org/10.1016/j.talanta.2023.124491. 

- [109] G.A. Bodkhe, M.S. More, A. Umar, A.A. Ibrahim, S. Siva, M.A. Deshmukh, N. N. Ingle, D.K. Gaikwad, M.-L. Tsai, T. Hianik, M. Kim, M.D. Shirsat, Enhanced detection of heavy metal ions using ag nanoparticles and single-walled carbon nanotubes within Cu-based metal-organic frameworks, J. Environ. Chem. Eng. 12 (2024) 113024, https://doi.org/10.1016/j.jece.2024.113024. 

- [110] K.B. Deore, S.B. Sitawar, N.N. Ingale, G.A. Bodke, M.-L. Tsai, T. Hainik, M. D. Shirsat, Synergistic enhancement of electrochemical sensing: EDTA@AgNP’s_ UIO-66 composite for sensitive and selective detection of toxic Hg(II) ions, 

   - Microchem. J. 209 (2025) 112766, https://doi.org/10.1016/j. microc.2025.112766. 

- [111] Z. Mirzaei Karazan, M. Roushani, S. Jafar Hoseini, Simultaneous electrochemical sensing of heavy metal ions (Zn2+, Cd2+, Pb2+, and Hg2+) in food samples using a covalent organic framework/carbon black modified glassy carbon electrode, Food Chem. 442 (2024) 138500, https://doi.org/10.1016/j. foodchem.2024.138500. 

- [112] M.R.J. Sarvestani, T. Madrakian, A.M. Tavassoli, M.M.M. Brukhani, A. Afkhami, M.A. Zolfigol, Synthesis of a triazine based COF and its application for the establishment of an electrochemical sensor for the simultaneous determination of Cd2+ and Pb2+ in edible specimens using Box-Behnken design, Food Chem. 464 (2025) 141606, https://doi.org/10.1016/j.foodchem.2024.141606. 

- [113] Q. Guo, Y. Zhang, L. Yan, X. Meng, Y. Wang, H. Zhai, X. Chen, X. Sun, Y. Guo, Y. Zhang, An ultrasensitive electrochemical sensor for detecting Cd(II) in aquatic products based on CS/COFs/PEDOT: PSS modified acupuncture needle electrode, Microchem. J. 197 (2024) 109846, https://doi.org/10.1016/j. microc.2023.109846. 

- [114] R. Zhang, H. Chen, Y. He, Y. Zhou, F. Yang, X. Yang, S. Wang, H. Bai, Field analysis electrochemical sensor based on hollow tube cluster covalent organic framework for sensitive detection of trace Pb(II) and As(V) in water samples, Microchem. J. 209 (2025) 112735, https://doi.org/10.1016/j. 

   - microc.2025.112735. 

- [115] L. Yu, X. Chen, L. Sun, Q. Zhang, B. Yang, M. Huang, B. Xu, Q. Xu, A covalent organic frameworks@gold nanoparticles@graphene nanocomposite based electrochemical sensor for simultaneous determination of trace Cd2+, Pb2+ and Cu2+, React. Funct. Polym. 194 (2024) 105770 https://doi.org/10.1016/j. reactfunctpolym.2023.105770. 

- [116] M.B. Behyar, A. Mirzaie, M. Hasanzadeh, N. Shadjou, Advancements in biosensing of hormones: recent progress and future trends, TracTrend Anal. Chem. 173 (2024) 117600, https://doi.org/10.1016/j.trac.2024.117600. 

- [117] S. Rawat, P. Phogat, Shreya, B. Chand, Advances in nanomaterial-based biosensors: innovations, challenges, and emerging applications, Mater. Today Commun. 48 (2025) 113334, https://doi.org/10.1016/j.mtcomm.2025.113334. 

- [118] Z. Chen, R. Feng, Q. Zhou, X. Zhang, Y. Fan, D. Fang, R. Zheng, W. Zhang, Z. Lu, J. Chen, Q.-W. Zhang, C. Jiang, P. Li, H. Yu, G. Li, Biomaterials and biosensing technologies in the detection and removal of pesticide residues: current trends and future prospects, Coord. Chem. Rev. 547 (2026) 217110, https://doi.org/ 10.1016/j.ccr.2025.217110. 

- [119] L. Cui, J. Wu, H. Ju, Electrochemical sensing of heavy metal ions with inorganic, organic and bio-materials, Biosens. Bioelectron. 63 (2015) 276–286, https://doi. org/10.1016/j.bios.2014.07.052. 

- [120] H. Ajab, M.H. Khan, P. Naveed, M.A. Abdullah, Evolution and recent development of cellulose-modified, nucleic acid-based and Green nanosensors for trace heavy metal ion analyses in complex media: a review, Int. J. Biol. Macromol. 307 (2025) 141745, https://doi.org/10.1016/j.ijbiomac.2025.141745. 

- [121] S. Zhan, Y. Wu, L. Wang, X. Zhan, P. Zhou, A mini-review on functional nucleic acids-based heavy metal ion detection, Biosens. Bioelectron. 86 (2016) 353–368, https://doi.org/10.1016/j.bios.2016.06.075. 

- [122] H. Bai, Y. Wang, X. Li, J. Guo, Electrochemical nucleic acid sensors: competent pathways for mobile molecular diagnostics, Biosens. Bioelectron. 237 (2023) 115407, https://doi.org/10.1016/j.bios.2023.115407. 

- [123] P. Song, Z. Fan, S. Sun, C. Sun, J. Wang, A novel electrochemical sensor of DNAzyme/AuNPs/Fe/ZIF-8/GCE for Pb2+ detection in the soil solution with enhanced sensitivity, anti-interference and stability, J. Environ. Chem. Eng. 12 (2024) 112349, https://doi.org/10.1016/j.jece.2024.112349. 

- [124] W. Bao, G. Aodeng, L. Ga, J. Ai, Nucleic acid aptamer-based biosensor for health monitoring: a review and future prospects, Microchem. J. 214 (2025) 113894, https://doi.org/10.1016/j.microc.2025.113894. 

- [125] S. Sawan, A. Errachid, R. Maalouf, N. Jaffrezic-Renault, Aptamers functionalized metal and metal oxide nanoparticles: recent advances in heavy metal monitoring, TracTrend Anal. Chem. 157 (2022) 116748, https://doi.org/10.1016/j. trac.2022.116748. 

- [126] J. Dong, D. Zhang, C. Li, T. Bai, H. Jin, Z. Suo, A sensitive electrochemical sensor based on PtNPs@Cu-MOF signal probe and DNA walker signal amplification for Pb2+ detection, Bioelectrochemistry 146 (2022) 108134, https://doi.org/ 10.1016/j.bioelechem.2022.108134. 

- [127] Y. Zhu, J. Gao, P. Xu, M. Zhang, Y. Tao, L. Qiao, H. Qin, Y. Zhang, Electrochemical sensor based on Y-shaped DNA by “one-pot” method for Mercury detection, Microchem. J. 204 (2024) 111013, https://doi.org/10.1016/j. microc.2024.111013. 

- [128] S. Li, H. Meng, H. A, Y. Zhang, H. Wang, W. Yang, P. Pang, An electrochemical biosensor for Mercury(II) detection based on DNA-Au bio-bar codes coupled with enzymatic dual signal amplification, Microchem. J. 207 (2024) 112195, https:// doi.org/10.1016/j.microc.2024.112195. 

- [129] X. Wang, M. Xu, Y. Kuang, X. Liu, J. Yuan, A novel ratiometric electrochemical aptasensor based on M-shaped functional DNA complexes for simultaneous detection of trace lead and Mercury ions in series aquatic edible vegetables, J. Hazard. Mater. 465 (2024) 133169, https://doi.org/10.1016/j. jhazmat.2023.133169. 

- [130] H. Jin, J. Dong, X. Qi, X. Sun, M. Wei, B. He, Z. Suo, A label-free impedance-based electrochemical sensor based on self-assembled dendritic DNA nanostructures for Pb2+ detection, Bioelectrochemistry 149 (2023) 108312, https://doi.org/ 10.1016/j.bioelechem.2022.108312. 

- [131] R. Wang, C.-Y. Xiong, Y. Xie, M.-J. Han, Y.-H. Xu, C. Bian, S.-H. Xia, Electrochemical sensor based on MoS2 nanosheets and DNA hybridization for 

16 

trace Mercury detection, Chin. J. Anal. Chem. 50 (2022) 100066, https://doi.org/ 10.1016/j.cjac.2022.100066. 

- [132] Y. Zhang, Z. Zhou, M. Yu, Y. Sun, S. Ying, L. Qian, Recent advances in laccase: enzyme discovery, molecular modification and application to electrochemical biosensors in nanomaterials, Microchem. J. 217 (2025) 114863, https://doi.org/ 10.1016/j.microc.2025.114863. 

- [133] B. Siritanaratkul, C.F. Megarity, Electrochemically-driven enzyme cascades: recent developments in design, control, and modelling, Curr. Opin. Electro 47 (2024) 101565, https://doi.org/10.1016/j.coelec.2024.101565. 

- [134] M.B. Gumpu, U.M. Krishnan, J.B.B. Rayappan, Design and development of amperometric biosensor for the detection of lead and Mercury ions in water matrix—a permeability approach, Anal. Bioanal. Chem. 409 (2017) 4257–4266, https://doi.org/10.1007/s00216-017-0376-9. 

- [135] H.S. Magar, M.E. Ghica, M.N. Abbas, C.M.A. Brett, Highly sensitive choline oxidase enzyme inhibition biosensor for lead ions based on multiwalled carbon nanotube modified glassy carbon electrodes, Electroanalysis 29 (2017) 1741–1748, https://doi.org/10.1002/elan.201700111. 

- [136] P.L. Kyabutwa, N. Alyamni, J.L. Abot, A.G. Zestos, Recent trends in electrochemical methods for real-time detection of heavy metals in water and soil: a review, Curr. Opin. Electro 54 (2025) 101749, https://doi.org/10.1016/j. coelec.2025.101749. 

- [137] C. You, Y. Cai, W. Wu, H. Zhang, X. Gao, Y. Song, Applications of machine learning in analysis and design of aerospace composite structures, Thin Wall Struct. 218 (2026) 113914, https://doi.org/10.1016/j.tws.2025.113914. 

- [138] G.S. Hida, A.C. Alves Do Nascimento, Overview of machine learning in class imbalance scenarios: trends, challenges, and approaches, Expert. Syst. Appl. 298 (2026) 129592, https://doi.org/10.1016/j.eswa.2025.129592. 

- [139] Y. Wang, Q. Zheng, Y. Yan, X. Bai, W. Chen, J. Jiang, J. Liu, M. Xu, Behavior recognition of spatial non-cooperative targets via geometric feature extraction: a random forest approach with deep neural network comparison, Aerosp. Sci. Technol. 168 (2026) 110902, https://doi.org/10.1016/j.ast.2025.110902. 

- [140] A. Moghadamnejad, M.A. Moghaddasi, M. Hamidia, R.K. Mohammadi, M. Zare, Ranking earthquake prediction algorithms: a comprehensive review of machine learning and deep learning methods, Soil. Dyn. Earthq. Eng. 200 (2026) 109740, https://doi.org/10.1016/j.soildyn.2025.109740. 

- [141] Y. Li, M. Zhang, X. Bian, L. Tian, C. Tang, Progress of independent component analysis and its recent application in spectroscopy quantitative analysis, 

_International Journal of Electrochemical Science 20 (2025) 101209_ 

Microchem. J. 202 (2024) 110836, https://doi.org/10.1016/j. microc.2024.110836. 

- [142] A. Peng, R. Huang, Research progress on the application of deep learning in fingerprint recognition, Pattern Recogn. 171 (2026) 112216, https://doi.org/ 10.1016/j.patcog.2025.112216. 

- [143] P.W. Harlina, V. Maritha, F. Geng, A. Nawaz, T. Yuliana, E. Subroto, H.J. Dahlan, E. Lembong, S. Huda, Comprehensive review on the application of omics analysis coupled with chemometrics in gelatin authentication of food and pharmaceutical products, Food Chem. X. 23 (2024) 101710, https://doi.org/10.1016/j. fochx.2024.101710. 

- [144] A. Roy, S. Chakraborty, Support vector machine in structural reliability analysis: a review, Reliab. Eng. Syst. Safe 233 (2023) 109126, https://doi.org/10.1016/j. ress.2023.109126. 

- [145] X. Xie, Y. Tian, J. Li, L. Wan, Shifting from physical models to learning methods for trajectory prediction: a review, Expert. Syst. Appl. 297 (2026) 129303, https://doi.org/10.1016/j.eswa.2025.129303. 

- [146] L. Liu, J. Xue, Y. Meng, T. Xu, M. Cong, Y. Ding, Y. Yang, Application of artificial neural networks to acoustic composites: a review, Mater. Today Commun. 45 (2025) 112342, https://doi.org/10.1016/j.mtcomm.2025.112342. 

- [147] R. Cai, J. Li, Y. Tan, J. Tang, X. Chen, Convolutional neural networks for construction safety: a technical review of computer vision applications, Appl. Soft Comput. 180 (2025) 113374, https://doi.org/10.1016/j.asoc.2025.113374. 

- [148] H. Yao, R. Wu, J. Zou, J. Liu, G. Peng, X. Wang, W. Zhou, S. Ai, L. Lu, A machine learning strategy-incorporated BiFeO3/Ti3C2 MXene electrochemical platform for simple, rapid detection of Pb2+ with high sensitivity, Chemosphere 340 (2023) 139728, https://doi.org/10.1016/j.chemosphere.2023.139728. 

- [149] V. Kailasam, R. Sankararajan, M. Kailasam, S.B. Suseela, Machine learning assisted metal Oxide-Bismuth oxy halide nanocomposite for electrochemical sensing of heavy metals in aqueous media, Cryst. Res. Technol. 59 (2024) 2300173, https://doi.org/10.1002/crat.202300173. 

- [150] S.A. Lahari, N. Kumawat, K. Amreen, R.N. Ponnalagu, S. Goel, IoT integrated and deep learning assisted electrochemical sensor for multiplexed heavy metal sensing in water samples, Npj. Clean. Water 8 (2025) 10, https://doi.org/ 10.1038/s41545-025-00441-x. 

- [151] Z. Tao, L. Su, M. Li, X. Xuan, C. Li, H. Li, A Sn-Ta-O-doped vertical graphene electrochemical sensor based on a machine learning prediction model for monitoring cadmium in beverages, Food Chem. 493 (2025) 145744, https://doi. org/10.1016/j.foodchem.2025.145744. 

17 


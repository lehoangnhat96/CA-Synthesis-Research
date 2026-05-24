# **INTEGRATED DYNAMIC MODEL OF THE ALKALINE DELIGNIFICATION PROCESS OF LIGNOCELLULOSIC BIOMASS** 

## **MODELO DINÁMICO INTEGRADO DEL PROCESO DE DESLIGNIFICACIÓN ALCALINA DE BIOMASA LIGNOCELULÓSICA** 

## JOHN FUERTEZ 

_M.Sc. Bioprocesos y Flujos Reactivos, Escuela de Procesos y Energía, Universidad Nacional de Colombia, Sede Medellín, jmfuerte@bt.unal.edu.co_ 

## ANGELA RUIZ 

_Ph.D. Bioprocesos y Flujos Reactivos, Profesor, Escuela de Procesos y Energía, Universidad Nacional de Colombia, Sede Medellín, aaruiz@bt.unal.edu.co_ 

## HERNÁN ALVAREZ 

_Ph.D.  Profesor, Escuela de Procesos y Energía, Universidad Nacional de Colombia, Sede Medellín,hdalvare@gmail.com_ 

## ALEJANDRO MOLINA 

_Ph.D. Bioprocesos y Flujos Reactivos, Profesor, Escuela de Procesos y Energía, Universidad Nacional de Colombia, Sede Medellín, amolinao@bt.unal.edu.co_ 

Received for review November  16[th] , 2010, accepted March  28[th] , 2011, final version May , 2[ th] , 2011 

**ABSTRACT:** Although in the public literature there are several studies that describe models of alkaline delignification, they were originally developed for the paper industry, and do not include the effects of important operating variables such as temperature, hydroxide-ion concentration, solid to liquid weight ratio, particle size, biomass composition (hemicellulose, lignin fraction) and mixing. This lack of detailed models of the pretreatment stages prompted the current study that describes a model which includes the variables listed above and provides an important tool for predicting the degree of lignin removal in lignocellulosic materials such as sugarcane bagasse (Saccharum officinarum L). The model considers kinetic expressions available in the literature. The kinetic parameters were determined by fitting the model to experimental data obtained for that purpose in our lab. The experimental matrix considered eighteen, 24-h isothermal experiments in which bulk and residual delignification stages were observed to occur in a parallel manner. Carbohydrate removal and hydroxide consumption were related to lignin removal by effective stoichiometric coefficients that were calculated by fitting the experimental data. A mixing compartment network model that represented mixing inside the reactor was included into a temporal superstructure based on the similarity between plug flow reactors and ideal batch reactors to model a non-ideally mixed batch reactor. The kinetic model was validated with data obtained in this study. **KEYWORDS** : Mathematical model, alkaline and Kraft delignification, pretreatment, lignocellulosic biomass, sugarcane bagasse 

**RESUMEN:** A pesar que en la literatura existen varios estudios que describen modelos de deslignificación alcalina, estos fueron desarrollados originalmente para la industria de papel, y no incluyen los efectos de las variables de operación importantes tales como temperatura, concentración del hidróxido, relación sólido-líquido, tamaño de partícula, composición de la biomasa (fracciones de hemicelulosa y lignina) y mezclado. Esta carencia de modelos detallados de las etapas del pretratamiento incitó el presente estudio que describe un modelo que incluye las variables mencionadas y proporcione una importante herramienta para predecir el grado de remoción de lignina en materiales lignocelulósicos tales como bagazo de caña de azúcar (Saccharum officinarum L). El modelo considera expresiones cinéticas disponibles en la literatura. Los parámetros cinéticos fueron determinados por ajuste a los datos experimentales obtenidos en nuestro laboratorio. La matriz experimental consideró dieciocho experimentos isotérmicos de 24horas en los cuales se observó que las etapas de deslignificación principal (bulk) y residual ocurrieron en paralelo. La remoción de carbohidratos y consumo de hidróxido fueron relacionados con la remoción de lignina mediante coeficientes estequiométricos efectivos que fueron calculados por ajuste a los datos experimentales. Un modelo de compartimientos de mezclado que representa la mezcla dentro del reactor fue incluido en una superestructura temporal basada en la similaridad entre los reactores del flujo pistón y reactores ideales por lotes para modelar un reactor por lote de  mezcla no ideal. El modelo cinético fue validado con los datos obtenidos en este estudio. 

**PALABRAS CLAVE:** Modelo matemático, deslignificación alcalina y Kraft, pretratamiento, biomasa lignocelulósica, bagazo de caña de azúcar 

Dyna, year 78, Nro. 170, pp. 175-184.  Medellin, December, 2011.  ISSN 0012-7353 

Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass - Fuertez et al 

**176** 

## **1.  INTRODUCTION** 

Extensive research could decrease the cost of the biomass pretreatment processes [1]. While most pretreatment methods are either physical or chemical, some incorporate both effects [1-3]. Alkali pretreatment technologies, such as lime pretreatment, are similar to the Kraft paper pulping technology. The major effect of alkaline pretreatment is the removal of lignin from biomass, thus improving the reactivity of the remaining polysaccharides [4]. 

Analogous to alkaline delignification in the paper industry, biomass pretreatment can be simplified as three parallel processes of lignin removal, all occurring at the same time, but with one dominating during different stages of the processes. The first process is an initial stage which takes place rapidly. Small parts of lignin molecules are dissolved by the breaking of phenolic α-0-4 links which are easy to break, and some β-0-4 links. The second process called main or bulk stage, involves the breaking of the β-aryl-ether (β0-4) links. The reaction rate is selective and carbohydrates dissolution is relatively low. Finally, in the residual stage, carbohydrates degradation is much slower than in the main stage and some carbon-carbon links of lignin break [5-8]. 

The existence of two or three stages for carbohydrates breakdown has caused some controversy [9]. However, Andersson et al. [10] and Johansson [11] observed three parallel stages during Kraft deslignification of softwood, as well as Gustavsson [12] who has considered that the reaction rate of carbohydrates follows a linear function of the delignification rate. 

Although there are a lot of alkaline and Kraft delignification models [9, 10, 13-17], they are generally used to describe the delignification process of the paper industry. Nevertheless, it seems possible to propose a model that considers effects such as particle size, solid-liquid ratio, temperature, and mixing intensity. The objective of this paper is to present such a model for the alkaline delignification of biomass, as pretreatment to produce ethanol from sugarcane bagasse (Saccharum officinarum L). 

## **2.  EXPERIMENTAL SECTION** 

## **2.1  Materials** 

Sugarcane bagasse is widely used for ethanol production [5, 18-22] and was the material selected in 

this study. It was provided by some farms located in the Department of Nariño (in the Southwest of Colombia). 

Raw sugarcane bagasse was manually cut to 2 cm-long pieces and dried at 45 ºC for 48 hours in a convection furnace, milled, sieved, and stored in sealed containers at 4 °C until it was used. The stored sugarcane bagasse had the following composition: 5.79 % humidity and 94.31 % dry weight with 13.34 % lignin, 42.88 % cellulose, and 27.38 % hemicellulose, in dry weight percentages. Reagent grade calcium hydroxide was used to carry out the delignification process. 

During the delignification reaction, samples were taken every 4 hours, until a 24 hour test was completed. 

The resulting mixture was neutralized with 1.8 N hydrochloric acid to determine hydroxide consumption and avoid interferences during lignin and hemicellulose determination. Finally, the samples were washed and dried during 48 hours at 45 ºC in a convection drying oven. 

## **2.2  Analysis Methods** 

The lignin and hemicellulose content of the solid phase was determined by using the VanSoest method [23]. Sieving and optical microscopy were used to estimate the average particle diameter. The hemicellulose content was calculated according to: 


![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0002-16.png)


All terms are explained in the nomenclature section. The remaining lignin fraction (L) was calculated as: 


![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0002-18.png)


Experimental conditions were defined according to the literature [4,6,18,24-26] and are summarized in Table 1. The experimental design consisted of two groups of isothermal tests. The first group (from F1 to F9) had a high liquid to solid ratio (R = 50 L/kg) and guaranteed an almost constant chemical concentration during the 

**177** 

Dyna 170, 2011 

delignification process. Experiments for the second group (from G1 to G9) were carried out at a low liquid to solid ratio (R = 12 L/kg) to identify changes in the hydroxide concentration. The liquor volume was 4.5 L, and 0.09 kg or 0.375 kg of biomass were added to obtain liquid to solid ratios of 50 L/kg and 12 L/kg, respectively. 

Experiments were carried out in a cramping bracket 316 stainless steel reactor with a 0.5 HP stirring system. The reactor had two baffles. The following are the most important geometric characteristics of the reactor and stirring system: tank diameter (DT): 0.205 m, tank height (LT): 0.205 m, baffle width (WB): 0.015 m, paddles inclined at 30º (axial flow impeller), impeller baffle height (LB): 0.13 m, 2-paddle blade agitator with diameter (DA): 0.17 m, agitator height from the reactor bottom (LA): 0.035 m, blade width (Wa): 0.03 m. 

## **3.3  Kinetics of the Hydroxide Reaction** 

In the initial stage, most hydroxide is consumed in the hydrolysis of acetyl groups that are associated with the hemicellulose, in the neutralization of acid products and in possible reactions of carbohydrate degradation. In the main stage, it is consumed in the neutralization of products formed during carbohydrates breakdown and lignin-phenolates formation. In the residual stage, hydroxide consumption is mainly due to the neutralization of products from the breakdown of carbohydrates. The change in the hydroxide concentration can be expressed as [16, 28]: 


![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0003-06.png)



![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0003-07.png)


In Eq. (5), q1 and q2 are empirical constants that are required because the real stoichiometry is unknown. 

## **3.  MODEL** 

## **3.1  Kinetics of Alkaline Delignification** 

The three-stage parallel model has been extensively used [5, 6, 22] to describe the alkaline delignification of material used in the ethanol production. According to this model and those reported by Dang and Nguyen [15,19, 27], the kinetic constant (ki) of a single first order kinetic equation included the effects of particle size, temperature, and reagents concentration to describe lignin dynamics: 


![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0003-12.png)



![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0003-13.png)


In the above equation, the hydroxide concentration follows a power law and the temperature dependence is given by an Arrhenius expression. The variable corresponding to the average particle diameter (δ) is introduced in the kinetic equation as well, in order to consider that effect in the chemical reaction. 

## **3.2  Kinetics of the Carbohydrate Reactions** 

This study considers a constant (g1) that determines the relation between hemicellulose and lignin kinetics for low temperatures (< 100 ºC). This approximation reduces the number of parameters, and it is required because the process stoichiometry is unknown. 


![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0003-17.png)



![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0003-18.png)


## **3.4  Mixing Effect** 

To consider mixing effects, we followed a temporal superstructure, similar to that established by Zhang and Smith [29] and summarized below the Reynolds number for agitated tanks with suspended solids (6), the apparent viscosity for pseudoplastic fluids (7). 


![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0003-21.png)



![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0003-22.png)



![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0003-23.png)



![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0003-24.png)


where the shear rate (γ) is calculated as: 


![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0003-26.png)



![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0003-27.png)


for laminar regime (Re < 10), according to Metzner and Otto [30], and 


![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0003-29.png)



![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0003-30.png)


for pseudoplastic fluids in turbulent flow, according to Sanchez et al. [31]. 

## **3.5. Time Intervals** 

Zhang and Smith [29] calculated the length of time intervals or mixing time (tm) as 4 times the circulation time, which is determined with the pumping capacity 

Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass - Fuertez et al 

**178** 

for one-phase systems. However, with solid materials in suspension, it is possible to use the following equation [32, 33]: 


![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0004-03.png)



![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0004-04.png)



![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0004-05.png)



![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0004-06.png)



![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0004-07.png)


Equation  (10) is valid for 97 % uniformity, a solid to liquid ratio of 5 kg/m[3] and a particle size larger than 0.1 mm.  The form factor was estimated using (12), which is valid for diameters from 0.1 mm to 2.8 mm [34]. 


![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0004-09.png)



![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0004-10.png)


## **3.6  Temperature program** 

In the experiments, the temperature was varied according to the temperature program in (13) and (14), which represents a temperature ramp followed by a constant temperature period: 


![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0004-13.png)


## **4.  PARAMETRIC ESTIMATION** 

The parametric determination of the kinetic parameters in the model was carried out with Matlab® _._ The experimental data of lignin kinetic were initially 

adjusted using the Matlab® nlinfit function, designed for nonlinear models, in order to estimate the kinetic reaction constant (ki) and the initial values of the degradable lignin fractions for the main stage (Losince the bulk (main) and residual delignification stages 1) were observed. A second step involved the linearization of the lignin kinetic constant (ki) and the Matlab® regress function was used to estimate: Ai, ai, Ei, ni, and wi. For the parametric estimation of the hemicellulose kinetics, hydroxide consumption, and mixing model parameters (g1, qi, λ), the Matlab® sim_anneal_MR function was used for nonlinear systems with multiple responses. The confidential intervals (CI) were calculated by each Matlab® function. 

Kim and Holtzapple [6] reported activation energies of 50.15 kJ/mol and 54.21 kJ/mol for the main and residual stages in the delignification of corn straw with calcium hydroxide under oxidative conditions. Similarly, Chiang and Yu [35] and Dolk et al. [36] reported that Ea varies between 120 kJ/mol and 130 kJ/mol for the main stage and between 110 kJ/mol and 119 kJ/mol for the residual stage when the raw material was wood. The activation energy values found in this study, presented in Table 2, are lower than those reported by Chiang and Yu [35] and Dolk et al. [36]. Given the highly empirical character of the model presented in this study, one needs to be careful when giving any physical interpretation to the kinetic values obtained after regression. Nevertheless, the low values of E1 and E2 could imply that sugarcane bagasse is more easily removed than corn straw or wood. Granda [5] and Sabatier et al. [22] reported values of activation energy for the alkaline delignification of sugarcane bagasse that varied between 4.56 kJ/mol and 42.04 kJ/mol depending on pretreatment. These values agree with those presented in Table 2. 

**Table 1.** Summary of experimental conditions 

||**Table 1.**Summaryof experimental conditions|
|---|---|
||**No.**<br>**T (ºC)**<br>**C (kg Ca(OH)2/kg biomass)**<br>**Average particle  diameter (mm)**<br>**Stirring rate  N* (rpm)**|
|||
|**Group 1 R**<br>**= 50 L/kg**|F1<br>40<br>0.3<br>0.455<br>100|
||F2<br>40<br>0.1<br>0.455<br>100|
||F3<br>60<br>0.3<br>0.455<br>100|
||F4<br>70<br>0.3<br>0.455<br>100|
||F5<br>40<br>0.5<br>0.455<br>100|
||F6<br>40<br>0.3<br>0.220<br>100|
||F7<br>40<br>0.3<br>1.065<br>100|
||F8<br>40<br>0.3<br>0.455<br>50|
||F9<br>40<br>0.3<br>0.455<br>200|



**179** 

Dyna 170, 2011 

||**No.**<br>**T (ºC)**<br>**C (kg Ca(OH)2/kg biomass)**<br>**Average particle  diameter (mm)**<br>**Stirring rate  N* (rpm)**|
|---|---|
|**Group 2 R**<br>**= 12 L/kg**|G1<br>40<br>0.3<br>0.455<br>100|
||G2<br>40<br>0.1<br>0.455<br>100|
||G3<br>60<br>0.3<br>0.455<br>100|
||G4<br>70<br>0.3<br>0.455<br>100|
||G5<br>40<br>0.5<br>0.455<br>100|
||G6<br>40<br>0.3<br>0.220<br>100|
||G7<br>40<br>0.3<br>1.065<br>100|
||G8<br>40<br>0.3<br>0.455<br>50|
||G9<br>40<br>0.3<br>0.455<br>200|



The (ai) exponential factor values for alkaline pretreatment with sugarcane bagasse has not been reported in refereed literature; however, Perez et al. [37] and Sixta and Rutkowska [38] found values similar to those presented in Table 2 for the Kraft delignification of Eucalyptus globulus; poplar white birch, maple sugar, and pine fiber. 

The effective coefficients values (qconsumption. As expected, a significant amount of i) show low hydroxide hydroxide is consumed by the hemicelluloses, possibly in the hydrolysis of acetyl groups, acid neutralization, and polymer degradation [5, 28]. 

## **4.1. Degradable Lignin Fraction (Loi)** 

The degradable lignin fraction of the main stage (Lo1) was adjusted to (15) using the Matlab® regress function. The fraction of residual stage (Lo2) was calculated as 1-Lo1.  The experiments showed that Lo1 increases with temperature and hydroxide concentration, and decreases when the average particle diameter (δ) increases. 


![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0005-07.png)



![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0005-08.png)


**Table 2** . Parameter values obtained after regression of the experimental data 

|**Parameter**|**Estimate**|**CI**|
|---|---|---|
|~~E~~1<br>(kJ/mol)<br>~~E~~2<br>(kJ/mol)<br>~~A~~1<br>(mmwi/ min (mol L-1)ai)|15.11<br>25.81<br>0.728|±0.084<br>±1.309<br>±0.258|



|**Parameter**|**Estimate**|**CI**|
|---|---|---|
|~~A~~2<br>(mmwi/ min (mol L-1)ai)|0.646|±0.235|
|~~a~~1|0.372|±0.061|
|~~a~~2|0.539|±0.006|
|~~w~~1|0.178|±0.021|
|~~w~~2|0.330|±0.029|
|~~q~~1|||
|(mol hydroxide/kg|4.500|±0.002|
|hemicellulose)|||
|~~q~~2|||
|(mol hydroxide /kg|3.005|±0.001|
|Lignin)|||



## **4.2. Effective Coefficient (g1)** 

The effective coefficient (g1) was adjusted to expression (16). This equation shows that by increasing temperature, hydroxide concentration, and material size there is an increase in the hemicellulose dissolution. This indicates that hemicellulose has a sensitive structure during the alkaline pretreatment and agrees with previous observations [5, 8, 11, 39]. 


![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0005-14.png)


## **4.3. Mixing Model Parameters** 

Mixing was approximated by three interconnected CSTRs that considered three mixing regions: the impeller section (Va), the main section (Vb), and the defined according to Zhang and Smith [29], leaving a baffle section (Vc). The volumes for each section were parameter free (Flow fraction, λ) that divides the flow into a temporary structure (see Fig.  1). The estimated value of (λ) was 0.730 ±0.015 m[3] min[-1] /m[3] min[-1] . 

Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass - Fuertez et al 

**180** 


![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0006-02.png)


**Figure 1.** Connection of mixing compartments, adapted from Zhang and Smith [29] 

Table 3 describes the different parameters used to simulate mixing. 

||0.220|2.318|
|---|---|---|
||||
|**100**|0.455|2.342|
||||
||1.065|2.367|
||||
|**200**|0.455|1.171|
||**12L/kg**||
||**δ  (mm)**||
|**50**|0.455|34.48|
||||
||0.220|17.09|
||||
|**100**|0.455|17.24|
||||
||1.065|17.39|
||||
|**200**|0.455|8.621|



**Table 3.** Input data for simulation of mixing in the reactor 

**Table 5.** Estimated values of apparent viscosity and flow regime 

|**Parameter**|**Value**|**Reference**|
|---|---|---|
|~~ρ~~<br>(kg/m3)<br>~~Np~~|1005<br>2.5|this work<br>[40]|
|~~n~~|0.88|[41]|
|~~K~~<br>(kg s(n-2)/m)<br>~~β~~|0.009<br>1.400|[41]<br>this work|
|~~α~~|0.010|this work|
|~~b~~|1.150|[32]|
|~~d~~|0.102|[32]|
|~~e~~<br>(ºK/min)|1.0782|this work|



## **5.  RESULTS** 

The values of each time constant for the temporary structure in the mixing model at different rates of stirring, liquid-solid relations, and average chips diameter after 2000 minutes of pretreatment are shown in Table 4.  The time interval was higher when the solids amount was higher (12L/kg liquid to solid ratio), and increased by increasing the average particle diameter (δ), but decreased by increasing the stirring rate. 

**Table 4.** Time intervals, temporal superstructure 

|~~**N***~~<br>**(rpm)**|<br> <br>**50L/kg**|~~**t***~~**m**<br> **(min)**|
|---|---|---|
||**δ  (mm)**||
|**50**|0.455|4.683|



|**N*(rpm)**|**μa* (mPa.s)**|**Re**|
|---|---|---|
|50|5.219|4637|
|100|4.570|10591|
|200|4.002|24189|



Table 5 presents estimated values of apparent viscosity and flow regime for the stirring levels evaluated in this work. The results are similar to those reported by Goncalves et al. [42] and Ruzene et al. [43], but slightly lower probably because of carbohydrates losses, a different particle size used in this study, and the undetermined stirring effects. 

The statistical characterization of a comparison between predicted and experimental values showed that the residuals varied between -0.06 and 0.04, following a Gaussian distribution with a small variance. The residual calculation was made as the difference between hemicellulose, lignin, and hydroxide consumption fractions for each prediction and the experimental data. The error was calculated as the sum of the squared residual. 

## **6.  MODEL VALIDATION** 

In order to validate the model predictions, a test of 48 hours with 0.3 kg of sugarcane bagasse and independent from the experimental design for the parametric estimation was carried out.  The conditions were: T* = 57 ºC, 0.24 kg Ca(OH)2/kg biomass, R = 15 L/kg biomass, δ = 0.77 mm, and N* = 150 rpm. 

**181** 

Dyna 170, 2011 

Figure 2 shows good adjustment between prediction and experiments when the following values were calculated t*m = 8.475 min, # intervals = 413, Re = 17.17, μa* = 4.229 mPa.s. 

Predictions with the model were compared as well with data from Granda [5] with relatively good success. A detailed comparison is given by Fuertez [44]. Similar model validation approaches can be explored in García et al. [45] and Montes et al. [46]. 


![](0 Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass_images/image-0007-04.png)


**Figure 2.** Comparison of model predictions (lines) with experimental data (points) for the variation of  a. Lignin, b. Hemicellulose and c. Hydroxide with time 

## **7.  CONCLUSIONS** 

The alkaline delignification process may be adequately modeled considering the effect of temperature, particle mean diameter, reagent concentration, liquid to solid ratio, and stirring effects using the model proposed in this paper. 

The sugarcane bagasse delignification happens faster as temperature and hydroxide concentration increase, while the material size and liquid to solid ratio decreases, in an environment with adequate mixing. 

The mixing model composed of batch reactors formed with a temporary superstructure of mixing compartments correctly describes the flow within the reactor and predicts the lignin, hemicellulose, and hydroxide kinetics during alkaline pretreatment. 

## **NOMENCLATURE** 

- µa apparent viscosity (Pa. s) µa* apparent viscosity (mPa. s) 

- γ shear rate (s[-1] ) K consistency index (kg s[(n-2)] /m) 

- n flow behavior index 

- k constant that depends on the system geometry N stirring rate (rps) 

- N* stirring rate (rpm) Re Reynolds number 

- Np power number DT reactor diameter (m) 

- VT reactor tank volume (m) 

- LT reactor tank height (m) W B width (baffles) (m) 

- Wa width (blades) (m) L B height (baffles) (m) 

- LA impeller height respect the reactor bottom (m) HL height (liquid) (m) 

- ρ suspension density (kg/m[3] ) 

- Da impeller diameter (m) M total mass (kg) 

- Ms biomass mass (kg) 

- T absolute temperature (ºK) T* temperature (ºC) To initial temperature (ºK) Tp isothermal operating temperature (ºK) e heating rate  (ºK/min) Li lignin fraction (kg lignin/kg initial lignin) 

Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass - Fuertez et al 

**182** 

|Lo|initial mass of lignin (kg)|
|---|---|
|Ls|kg remaining lignin at time t/kg dry matter|
|Lso|kg initial lignin/kg dry matter|
|Loi|degradable lignin fraction, stage i (kg lignin/|
||kg initial lignin)|
|Y|dry matter fraction (kg dry matter/kg|
|g1|biomass mass)<br>effective coeffcient (kg hemicellulose/kg|
|q1|lignin)<br>effective coeffcient (mol hydroxide/kg|
|q2|hemicellulose)<br>effective coeffcient (mol hydroxide /kg lignin)|
|V|volume of liquor (L)|
|Rs|solid-liquid relation (kg/m3)|
|Rc|universal gas constant (J/mol ºK)|
|θ|form factor|
|β|correction factor associated with the solid|
||concentration|
|α|correction factor associated with the form factor|
|d|constant equation|
|b|constant equation|
|dp|average particle diameter (mm)|
|Cs|hemicellulose matter (kg remanent|
||hemicellulose)|
|COH<br>-|hydroxide concentration (mol/L)|
|t|time (min)|
|tm|mixing time (s)|
|tm*|mixing time (min)|
|Ai|preexponential factor (mmwi/ min (mol L-1)ai)|
|δ|chips average diameter (mm)|
|Ei|activation energy, stage I (J/mol)|
|Ei*|activation energy, stage I (kJ/mol)|
|ai|associate constant, hydroxide concentration|
|in|the stage I|
|wi|associate constant, particle size in the stage I|
|ki<br>vo<br>λ|kinetic constant, stage I  (min-1)<br>volumetric fow (m3/min)<br>fow fraction (m3min-1/m3min-1)|
|Va|volume of the impeller section (m3)|
|Vb<br>Vc|volume of the main section (m3)<br>volume of the baffes section (m3)|



## **REFERENCES** 

[1] Chandel ak, ES C., Rudravaram, R., Narasu, ML., Rao, LV. and Ravindra, P., Economics and environmental impact of bioethanol production technologies: an appraisal. Biotechnol Molec Biol Rev, 2, pp. 14–32, 2007. 

[2]  Mcmillan, J.D., Pretreatment of lignocellulosic biomass. Enzymatic Conversion of Biomass for Fuels Production, ACS Symposium Series, ACS, Washington, 566, pp. 292–324. 1994. 

[3]  Mcmillan, JD., Bioethanol production: status and prospects. Renew Energy, 10,  pp. 295–302, 1997. 

[4]   Mosier, N., Wyman, C., Dale, B., Elander, R., Lee, Y., Holtzapple, M. and Ladisch, M., Features of promising technologies for pretreatment of lignocellulosic biomass. Bioresource Technology, 96, pp. 673–686. 2005. 

[5]   Granda, C., Sugarcane juice extraction and preservation, and long-term lime pretreatment of bagasse. [Tesis doctoral]. Texas A&M University, Ingeniería Química. 2004. 

[6]  Kim, S. and Holtzapple, M., Delignification kinetics of corn stover in lime pretreatment. Bioresource Technology, 97, pp. 778-7852006. 

[7]  Mocchiutti, P., Fundamentos de la producción de pastas celulósicas - Tema II – 1: Pulpado Químico - Pulpado Alcalino. 2007. 

[8]  Sierra, R., Granda, C., Holtzapple, M.T., Lime Pretreatment. Jonathan R. Mielenz (ed.), Biofuels: Methods and Protocols, Methods in Molecular Biology, 581, pp. 115-124, 2009. 

[9]  Gustafson, R., Sleicher, C. and Mckean, W., Theoretical Model of the Kraft Pulping Process, Ind. Eng. Chem. Process Design and Development, 22(1), pp. 87-96, 1983. 

[10]  Andersson, N., Wilson, D. and Germard, U., An improved kinetic model structure for softwood kraft cooking. Nordic Pulp and Paper Research Journal, 18 (2), pp. 200209. 2003. 

[11]  Johansson, D., Carbohydrate degradation and dissolution during Kraft cooking. [Licentiate thesis]. Karlstad University Studies, 2008. 

[12]  Gustavsson, G., On the interrelation between kraft cooking conditions and pulp composition. [Tesis Doctoral]. Royal Institute of Technology, Department of Fibre and Polymer Technology Division of Wood Chemistry and Pulp Technology, Stockholm, 2006. 

[13]  Bogrena, J., Brelida H. and Theliandera, H., Evaluating reaction kinetic models using well-defined kraft delignification data. Technical Articles, pp. 1-11, 2008. 

**183** 

Dyna 170, 2011 

[14] Castro, J., Baptista, C., Carvalho M., Egas, A. and Simao, J., Heterogeneous studies in pulping of wood: Modelling mass transfer of alkali. Chemical Engineering Journal, 139,  pp. 615-621, 2008. 

[15] Dang. V. and Nguyen, K., Characterisation of the heterogeneous alkaline pulping kinetics of hemp woody core. Bioresource Technology,  97, 1353-1359, 2006. 

[16]  Giudici R. and Won S., Kinetic model for kraft pulping of hardwood. Industrial and Engineering Chemistry Research. Ind. Eng. Chem. Res, 35,  pp. 856-863, 1996. 

[17] Yang, L. and Liu, S., Kinetic model for Kraft pulping process. Eng. Chem. Res,  44, pp. 7078–7085, 2005. 

[18] Chang, V.S., Nagwani, M. and Holtzapple, M.T., Lime pretreatment of crop residues bagasse and wheat straw. Applied Biochemistry and Biotechnology, 74, pp. 135–159, 1998. 

[19] Dang, V. and Nguyen, K., A Universal kinetic model for characterisation of the effect of chip thickness on Kraft pulping. Short Communication. Bioresource Technology, 99, pp. 1486-1490, 2008. 

[20]  Dawson, L. and Boophaty, R., Cellulosic ethanol production from sugarcane bagasse without enzymatic saccharification. BioResources, 3(2), pp. 452-460, 2008. 

[21] Hernandez, J., Comparative hydrolysis and fermentation of sugarcane and agave bagasse. Centro de Investigación en Biotecnologia Aplicada del Instituto Politécnico Nacional (CIBA-IPN), México. 2009. 

[22] Sabatier, J., Peniche, C. and Fernández, N., Soda pulping of bagasse: Delignification phases and kinetics. Holzforschung. 47. pp. 313-317, 1993. 

[23]  Mora, I., Nutrición animal. Primera Edición. Ed Universidad Estatal a Distancia San José. Costa Rica, 120, 1991. 

[24]  Chang, V.S. and Holtzapple, M.T., Lime pretreatment of switchgrass. Applied Biochemistry and Biotechnology. pp. 63-65, 3-19, 1997. 

[25] Karr, W. E. and Holtzapple, T., Using lime pretreatment to facilitate the enzymatic hydrolysis of corn stover. Biomass Bioenergy, 18, pp. 189–199, 2000. 

[26]  Playne, M.J., Increased digestibility of bagasse by pretreatment with alkalis and steam explosion. Biotechnology 

and Bioengineering, 26 (5), pp. 426–433, 1984. 

[27]  Dang, V. and Nguyen, K., A universal kinetic equation for characterising the fractal nature of delignification of lignocellulosic materials. Cellulose,  14, pp. 153-160. 2007. 

[28]  Santos, A., Rodríguez, F., Gilarranz, M., Moreno, D. and García, F., Kinetic modeling of kraft delignification of eucalyptus globules. Ind. Eng. Chem. Res, 36 (10), pp. 4114–4125, 1997. 

[29]  Zhang, J. and Smith, R., Design and optimization of batch and semi-batch reactors. Chem. Eng. Sci, 59, pp. 459 –478. 2004. 

[30]  Bhole, M. and Ford, C., Bennington, CPJ., Characterization of axial flow impellers in pulp fiber suspensions. 13th European Conference on Mixing London, 2009. 

[31]  Sánchez, J., Rodríguez, E., Casas. J., Fernández J. and Chisti Y., Shear rate in stirred tank and bubble column bioreactors. Chemical Engineering Journal 124, pp. 1–5, 2006. 

[32] Kuznamié, N. and Ljubieié, B., Suspension of floating solids with up-pumping pitched blade impellers; mixing time and power characteristics. Chemical Engineering Journal 84, pp. 325–333. 2001 

[33]Kuznamié, N., Zanetié, R. and Akrap, M., Impact of floating suspended solids on the homogenisation of the liquid phase in dual-impeller agitated vessel. Chemical Engineering and Processing 47, pp. 663–669. 2008. 

[34]  Roca, G., Sanchez, C., Gómez, E. and Barbosa, L., Caracterización del bagazo de la caña de azúcar. Parte I: características físicas. An. 6. Enc. Energ. Meio Rural, 2006. 

[35]  Chiang, VL. and Yu, J., Isothermal reaction kinetics of kraft delignification of Douglasfir. Journal of Wood Chemistry and Technology 10(3), pp. 293-310, 1990 

[36] Dolk, M., Yan, J. and Mccarthy., Kinetics of delignification of western hemlock in flow through reactors under alkaline conditions. Holzforschung, 43(2) pp. 91-98, 1989. 

[37] Pérez, J., Gilarranz, M., Rodríguez, F., Oliet, M. and García, J., Estudio sobre la cinética de la deslignificación en la fase residual de las cocciones kraft. Congreso Iberoamericano de investigación en celulosa y papel. pp 1-9,  2000. 

Integrated dynamic model of the alkaline delignification process of lignocellulosic biomass - Fuertez et al 

**184** 

[38] Sixta, H. and Rutkowska, E., Modeling of eucalyptus globulus kraft pulping. Lenzing AG Process Innovation, pp. 1-7. 2006. 

[39]  Taherzadeh, M J. and Karimi, K., Pretreatment of Lignocellulosic Wastes to Improve Ethanol and Biogas Production: A Review. Int. J. Mol. Sci, 9, pp. 1621-1651, 2008. 

[40]  Martín, A., Agitation and mixing. Suspension of solid particles. Chapter 9.  2003. 

[41] Karim, K., Thoma, G. and Al-Dahhan., Gas-lift digester configuration effects on mixing effectiveness. Water research 41. pp 3051 – 3060, 2007. 

[42] Goncalves, A., Costa, S. and Esposito, E., Panus trigrinus strains used in delignification of sugarcane bagasse prior to kraft pulping. Applied Biochemistry and Biotechnology. pp. 373-382, 2002. 

[43] Ruzene, DS., Goncalves, A., Teixeira, J. and Pessoa, M., Carboxymethylcellulose obtained by ethanol/water organosolv process under acid conditions. Applied biochemistry and Biothecnology vol. 136-140. 2007. 

[44] Fuertez, J., Modelo dinámico integrado de base fenomenológica del proceso de deslignificación por precipitación alcalina de material lignocelulósico. [Tesis de Maestría]. Universidad Nacional de Colombia Sede Medellín. 200, 2010. 

[45] García, E., Osorio, J. y Cortés, M. Modelamiento matemático de flujo bifásico: efecto de la velocidad de onda de presión sobre la magnitud y distribución de presiones. Dyna, Año 75, Nro. 154,  pp. 47-58. Medellín, Marzo de 2008. 

[46] Montes, E., Torres, R., Andrade, R., Pérez, O., Marimón, J. y Meza, I.  Modelado de las isotermas de desorción del ñame. Dyna, Año 76, Nro. 157, pp. 145-152.  Medellín, Marzo de 2009. 


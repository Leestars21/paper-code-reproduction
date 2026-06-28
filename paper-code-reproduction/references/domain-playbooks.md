# Scientific Domain Playbooks

Use this file after classifying the paper type. Pick the closest branch and follow its checklist.

## 1. Physics-Informed or PDE-Constrained Learning

Use this branch for PINNs, Deep Ritz variants, operator learning with PDE losses, or hybrid data-plus-physics training.

### What to recover first

- governing equation,
- boundary and initial conditions,
- residual formulation,
- collocation or sampling strategy,
- loss weights,
- nondimensionalization or unit scaling.

### Common failure modes

- residual loss dominates or vanishes,
- boundary conditions are implemented incorrectly,
- unit scaling makes optimization unstable,
- reported convergence depends on hidden curriculum or sampling policy.

### Minimum evidence

- one plot of each loss term over training,
- one physics residual summary,
- one boundary-condition satisfaction check,
- one comparison between pure data loss and hybrid loss if feasible.

## 2. Surrogate Model for Simulation, Experiment, or Response Prediction

Use this branch for simulation surrogates, reduced-order emulators, response predictors, and fast inference replacements for expensive experiments or solvers.

### What to recover first

- simulator or source solver,
- parameter range,
- interpolation vs extrapolation regime,
- input encoding,
- output granularity,
- evaluation split logic.

### Common failure modes

- training data covers a narrower regime than claimed,
- model succeeds only in interpolation,
- output normalization breaks physical meaning,
- evaluation hides difficult load cases.

### Minimum evidence

- parity plot or predicted-vs-reference plot,
- worst-case or hard-case example instead of average-only reporting,
- interpolation/extrapolation split if possible,
- one figure showing where the surrogate fails.

## 3. Inverse Problem or Parameter Identification

Use this branch for material identification, parameter recovery, latent property estimation, and observation-to-parameter mapping.

### What to recover first

- forward model,
- observed signals,
- unknown parameters,
- regularization,
- identifiability assumptions,
- noise model.

### Common failure modes

- inverse target is not uniquely identifiable,
- regularization is unstated,
- paper reports parameter accuracy without signal reconstruction quality,
- small noise changes produce unstable recovered parameters.

### Minimum evidence

- parameter error table,
- signal reconstruction comparison,
- sensitivity to noise or initialization if feasible,
- note on identifiability confidence.

## 4. Structured Scientific Model With Machine Learning

Use this branch for learned domain laws, structured response models, path-dependent behavior, hysteresis-like dynamics, and constrained scientific surrogates.

### What to recover first

- state variables,
- path, protocol, or condition definition,
- history dependence,
- material, subject, system, or regime class,
- physical, semantic, thermodynamic, monotonicity, or conservation constraints,
- unit conventions.

### Common failure modes

- curve fit looks good but violates domain constraints,
- path dependence is not preserved,
- training/test split leaks neighboring loading histories,
- energy consistency is ignored.

### Minimum evidence

- response comparison curves,
- peak and area-under-curve comparison,
- at least one nontrivial loading path example,
- note on domain plausibility and constraint satisfaction.

## 5. Biomedical, Medical Imaging, or Subject-Specific Models

Use this branch for subject-specific geometry, imaging-derived modeling, sensor-driven biomedical prediction, or patient-level prediction.

### What to recover first

- subject/specimen split logic,
- geometry preprocessing,
- acquisition protocol,
- target anatomy or tissue,
- evaluation granularity per subject, per slice, or per sequence.

### Common failure modes

- patient leakage,
- geometry normalization hiding physically important variation,
- subject-specific priors omitted from the paper,
- metrics look good but clinically or domain-implausible outputs remain.

### Minimum evidence

- subject-level split summary,
- one subject-specific qualitative comparison,
- one aggregate metric table,
- explicit note on sample size and uncertainty.
